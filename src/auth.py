from flask import Blueprint

auth = Blueprint("Auth", __name__, url_prefix="/api/v1/auth")


@auth.post("/register")
def register():
    return {"message": "User Created"}


@auth.get("/me")
def me():
    return {"message": "Me fetched"}
