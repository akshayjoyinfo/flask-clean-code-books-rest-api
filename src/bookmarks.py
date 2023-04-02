from flask import Blueprint

bookmarks = Blueprint("Bookmarks", __name__, url_prefix="/api/v1/bookmarks")


@bookmarks.get("/")
def get_all_books():
    return {
        "bookmarks": []
    }

