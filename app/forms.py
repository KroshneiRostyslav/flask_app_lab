from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, Regexp

class ContactForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[
            DataRequired(message="Ім'я обов'язкове"),
            Length(min=4, max=10, message="Від 4 до 10 символів")
        ]
    )

    email = EmailField(
        "Email",
        validators=[
            DataRequired(message="Email обов'язковий"),
            Email(message="Некоректний email")
        ]
    )
    
    phone_number = StringField(
        "Phone Number",
        validators=[
            DataRequired(message="Номер телефону обов'язковий"),
            Regexp(
                r'^\+380\d{9}$',
                message="Введіть дійсний номер телефону"
            )
        ]
    )
    
    subject = SelectField(
        "Subject",
        validators=[DataRequired(message="Виберіть тему")],
        choices=[
            ("", "-Select subject-"),
            ("question", "Question"),
            ("support", "Support"),
            ("feedback", "Feedback"),
            ("bug_report", "Report a Bug"),
            ("other", "Other")
        ]
    )

    message = TextAreaField(
        "Message",
        validators=[
            DataRequired(message="Повідомлення обов'язкове"),
            Length(max=500, message="Максимальна довжина 500 символів")
        ]
    )
    
    submit = SubmitField("Send")