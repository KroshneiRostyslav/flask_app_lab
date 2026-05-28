from datetime import datetime
from sqlalchemy import Enum
from .. import db

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(
        Enum("news", "publication", "tech", "other", name="post_category"),
        default="other",
        nullable=False
    )

    def __repr__(self):
        return f"<Post {self.id} | {self.title[:20]}>"
