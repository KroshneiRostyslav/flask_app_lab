from app import db
from datetime import datetime, UTC
from sqlalchemy import Enum

post_tags = db.Table(
    "post_tags",

    db.Column(
        "post_id",
        db.Integer,
        db.ForeignKey("posts.id")
    ),

    db.Column(
        "tag_id",
        db.Integer,
        db.ForeignKey("tags.id")
    )
)

class Post(db.Model):

    __tablename__ = "posts"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(150),
        nullable=False
    )

    content = db.Column(
        db.Text,
        nullable=False
    )

    posted = db.Column(
        db.DateTime,
        default=lambda: datetime.now(UTC)
    )

    category = db.Column(
        db.String(50)
    )

    author_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    author = db.relationship(
        "User",
        back_populates="posts"
    )

    tags = db.relationship(
        "Tag",
        secondary=post_tags,
        back_populates="posts"
    )

class Tag(db.Model):

    __tablename__ = "tags"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )

    posts = db.relationship(
        "Post",
        secondary=post_tags,
        back_populates="tags"
    )

    def __repr__(self):

        return f"<Tag {self.name}>"