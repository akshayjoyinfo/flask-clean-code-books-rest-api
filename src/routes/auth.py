from flasgger import swag_from
from flask import Blueprint, current_app, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
import validators
from src.models.user import UserModel
from src.constants.http_status_codes import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_200_OK, HTTP_401_UNAUTHORIZED
from src.services import API_PREFIX
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity

AUTH_PREFIX: str = "/auth"
auth = Blueprint("Auth", __name__, url_prefix=API_PREFIX + AUTH_PREFIX)


@auth.post("/register")
@swag_from('../docs/auth/register.yaml')
def register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    current_app.logger.info('User registration request received ', extra={
        'username': username,
        'email': email
    })

    if len(password) < 6:
        return jsonify({'error': 'Password too short'}), HTTP_400_BAD_REQUEST

    if not validators.email(email):
        return jsonify({'error': 'Wrong email format'}), HTTP_400_BAD_REQUEST

    if UserModel.find_by_email(email) is not None:
        return jsonify({'error': 'Email was taken'}), HTTP_409_CONFLICT

    hashed_password = generate_password_hash(password)

    new_user = UserModel(username=username, password=hashed_password, email=email)
    new_user.save_to_db()

    current_app.logger.info('User Created ', extra={
        'username': username,
        'email': email
    })
    return dict(message='User Created', user={
        'username': new_user.username,
        'email': new_user.email

    })


@auth.post("/login")
@swag_from('../docs/auth/login.yaml')
def login():
    email = request.json.get('email', '')
    password = request.json.get('password', '')
    current_app.logger.info("User is trying to login", extra={
        'username': email
    })

    existing_user = UserModel.find_by_email(email)

    if existing_user:
        is_pass_correct = check_password_hash(existing_user.password, password)

        if is_pass_correct:
            additional_claims = {"username": existing_user.username, "email": existing_user.email,
                                 "is_admin": existing_user.is_admin}
            refresh = create_refresh_token(identity=existing_user.id, additional_claims=additional_claims)
            access = create_access_token(identity=existing_user.id, additional_claims=additional_claims)

            return jsonify({
                'user': {
                    'refresh': refresh,
                    'access': access,
                    'username': existing_user.username,
                    'email': existing_user.email
                }

            }), HTTP_200_OK

    return jsonify({'error': 'Wrong credentials'}), HTTP_401_UNAUTHORIZED


@auth.get("/me")
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = UserModel.find_by_id(user_id)
    current_app.logger.info("Fetching me", extra={
        'username': user.username,
        'email': user.email
    })

    return {
        'username': user.username,
        'email': user.email
    }, HTTP_200_OK
