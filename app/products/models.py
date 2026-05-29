from app import db

from sqlalchemy.sql import func


class Category(db.Model):

    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    products = db.relationship(
        "Product",
        backref="category",
        lazy=True
    )

    def __repr__(self):

        return f"<Category {self.name}>"


class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(100),
        nullable=False
    )

    price = db.Column(
        db.Float,
        nullable=False
    )

    active = db.Column(
        db.Boolean,
        nullable=False,
        default=True,
        server_default="1"
    )

    created_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id")
    )

    def __repr__(self):

        return f"<Product {self.name}>"