from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
import validators
from flasgger import swag_from

from src.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED
from src.models.bookmark import BookmarkModel
from src.routes import API_PREFIX

BOOKMARKS_PREFIX: str = "/bookmarks"
bookmarks = Blueprint("Bookmarks", __name__, url_prefix=API_PREFIX + BOOKMARKS_PREFIX)


@bookmarks.post("")
@jwt_required()
@swag_from('../docs/bookmarks/create.yaml')
def create_bookmark():
    current_user = get_jwt_identity()

    body = request.get_json().get('body', '')
    url = request.get_json().get('url', '')

    if not validators.url(url):
        return jsonify({
            'error': 'Enter a valid url'
        }), HTTP_200_OK

    bookmark = BookmarkModel(body=body, url=url, visits=1, user_id=current_user)

    bookmark.save_to_db()

    current_app.logger.info('Bookmark created', extra={
        'result': 'Bookmark Created',
    })
    print('2222222sdfgsdffsfsdfsdf ')
    return jsonify({
        'message': 'Bookmark Created',
    }), HTTP_201_CREATED


@bookmarks.get("")
@jwt_required()
def get_bookmarks():
    current_user = get_jwt_identity()
    page = request.args.get('page', 1, type=int)
    per_page= request.args.get('count', 10, type=int)

    current_app.logger.info('Bookmarks received', extra={
        'page': page,
        'per_page': per_page,
    })

    bookmarks = BookmarkModel.find_all_paginate(page=page, per_page=per_page, user_id=current_user)


    data: list[BookmarkModel] = []
    for item in bookmarks.items:
        data.append({
            'id': item.id,
            'body': item.body,
            'url': item.url,
            'short_url': item.short_url
        })
    return jsonify({
         'results': data,
         'meta': {
             'page': bookmarks.page,
             'pages': bookmarks.page,
             'total_count': bookmarks.total,
             'prev_page': bookmarks.prev_num,
             'next_page': bookmarks.next_num,
             'has_next': bookmarks.has_next,
             'has_prev': bookmarks.has_prev
         }
    }), HTTP_200_OK
