from flask import Blueprint, request, jsonify
from models import BlogPost
from database.db_setup import db

blog_blueprint = Blueprint('blog', __name__, url_prefix='/api/blogs')

@blog_blueprint.route('/', methods=['GET'])
def get_all_posts():
    posts = BlogPost.query.all()
    return jsonify([
        {"id": post.id, "title": post.title, "content": post.content, "author": post.author, "created_at": post.created_at}
        for post in posts
    ])

@blog_blueprint.route('/<int:id>', methods=['GET'])
def get_single_post(id):
    post = BlogPost.query.get_or_404(id)
    return jsonify({
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "author": post.author,
        "created_at": post.created_at
    })

@blog_blueprint.route('/', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = BlogPost(
        title=data['title'],
        content=data['content'],
        author=data['author']
    )
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created successfully"}), 201

@blog_blueprint.route('/<int:id>', methods=['PUT'])
def update_post(id):
    post = BlogPost.query.get_or_404(id)
    data = request.get_json()
    post.title = data['title']
    post.content = data['content']
    post.author = data['author']
    db.session.commit()
    return jsonify({"message": "Post updated successfully"})

@blog_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Post deleted successfully"})
