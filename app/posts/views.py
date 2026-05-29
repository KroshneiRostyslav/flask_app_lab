from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    request
)

from app.posts import post_bp
from app.posts.models import Post, Tag
from app.posts.forms import PostForm
from app.posts.users import User
from app import db

@post_bp.route("/")
def home():
    return redirect(url_for("posts.all_posts"))

# ALL POSTS
@post_bp.route("/post")
def all_posts():

    posts = Post.query.order_by(
        Post.posted.desc()
    ).all()

    return render_template(
        "posts/all_posts.html",
        posts=posts
    )

# CREATE
@post_bp.route("/post/create", methods=["GET", "POST"])
def create_post():

    form = PostForm()

    form.author.choices = [
        (u.id, u.username)
        for u in User.query.all()
    ]

    form.tags.choices = [
        (t.id, t.name)
        for t in Tag.query.all()
    ]

    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            category=form.category.data,
            author_id=form.author.data
        )

        selected_tags = Tag.query.filter(
            Tag.id.in_(form.tags.data)
        ).all()

        post.tags = selected_tags

        db.session.add(post)
        db.session.commit()

        flash("Post created successfully", "success")

        return redirect(url_for("posts.all_posts"))

    return render_template(
        "posts/add_post.html",
        form=form
    )

# DETAIL
@post_bp.route("/post/<int:id>")
def detail_post(id):

    post = Post.query.get_or_404(id)

    return render_template(
        "posts/detail_post.html",
        post=post
    )

@post_bp.route("/post/<int:id>/update", methods=["GET", "POST"])
def update_post(id):

    post = Post.query.get_or_404(id)

    form = PostForm(obj=post)

    form.author.choices = [
        (u.id, u.username)
        for u in User.query.all()
    ]

    form.tags.choices = [
        (t.id, t.name)
        for t in Tag.query.all()
    ]

    if request.method == "GET":
        form.author.data = post.author_id
        form.tags.data = [tag.id for tag in post.tags]

    if form.validate_on_submit():

        post.title = form.title.data
        post.content = form.content.data
        post.category = form.category.data
        post.author_id = form.author.data

        post.tags.clear()

        selected_tags = Tag.query.filter(
            Tag.id.in_(form.tags.data)
        ).all()

        for tag in selected_tags:
            post.tags.append(tag)

        db.session.commit()

        flash("Post updated successfully", "warning")

        return redirect(
            url_for("posts.detail_post", id=post.id)
        )

    return render_template(
        "posts/add_post.html",
        form=form
    )

# DELETE
@post_bp.route("/post/<int:id>/delete", methods=["GET", "POST"])
def delete_post(id):

    post = Post.query.get_or_404(id)

    if request.method == "POST":

        db.session.delete(post)
        db.session.commit()

        flash("Post deleted", "danger")

        return redirect(url_for("posts.all_posts"))

    return render_template(
        "posts/delete_confirm.html",
        post=post
    )