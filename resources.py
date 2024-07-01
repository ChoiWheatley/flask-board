from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from models import Post

blp = Blueprint(
    "posts", __name__, url_prefix="/posts", description="Operations on posts"
)


@blp.route("/")
class Posts(MethodView):
    def get(self):
        posts = Post.query.all()
        return [post.to_dict() for post in posts], 200

    def post(self):
        data = request.get_json()
        new_post = Post(title=data["title"], content=data["content"])
        db.session.add(new_post)
        db.session.commit()

        return new_post.to_dict(), 201


@blp.route("/<int:post_id>")
class PostById(MethodView):
    def get(self, post_id):
        post = Post.query.get_or_404(post_id)
        return post.to_dict(), 200

    def put(self, post_id):
        post: Post = Post.query.get_or_404(post_id)
        data: dict = request.get_json()

        post.title = data["title"]
        post.content = data["content"]

        db.session.commit()
        return post.to_dict(), 200

    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()

        return "", 204
