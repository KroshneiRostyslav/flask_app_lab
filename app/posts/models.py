from app import db
from datetime import datetime
from sqlalchemy import Enum

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)

    content = db.Column(db.Text, nullable=False)

    posted = db.Column(db.DateTime, default=datetime.utcnow)

    category = db.Column(
        Enum("news", "publication", "tech", "other"),
        default="other"
    )

    author = db.Column(db.String(20), default="Anonymous")

    def __repr__(self):
        return f"<Post {self.title}>"