from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    SelectField,
    SelectMultipleField,
    SubmitField
)

from wtforms.validators import DataRequired
from app.posts.users import User
from app.posts.models import Tag

class PostForm(FlaskForm):

    title = StringField(
        "Title",
        validators=[DataRequired()]
    )

    content = TextAreaField(
        "Content",
        validators=[DataRequired()]
    )

    category = SelectField(
        "Category",
        choices=[
            ("news", "News"),
            ("publication", "Publication"),
            ("tech", "Tech"),
            ("other", "Other")
        ]
    )

    author = SelectField(
        "Author",
        coerce=int
    )

    tags = SelectMultipleField(
        "Tags",
        coerce=int
    )
    
    submit = SubmitField("Save")