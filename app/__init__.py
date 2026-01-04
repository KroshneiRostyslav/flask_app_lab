from flask import Flask, render_template, flash, redirect, url_for
from .forms import ContactForm
import logging

app = Flask(__name__)
app.secret_key = b'secret_key'

app.config.from_pyfile(r'..\config.py')

contact_logger = logging.getLogger("contact_form")
contact_logger.setLevel(logging.INFO)

handler = logging.FileHandler("contacts.log")
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
handler.setFormatter(formatter)

contact_logger.addHandler(handler)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contacts', methods=["GET", "POST"])
def contacts():
    form = ContactForm()

    if form.validate_on_submit():
        try:
            contact_logger.info(
                "Name=%s | Email=%s | Phone=%s | Subject=%s | Message=%s",
                form.name.data,
                form.email.data,
                form.phone_number.data,
                form.subject.data,
                form.message.data
            )

            flash(f"Повідомлення від {form.name.data} {form.email.data} успішно надіслано", "success")
        except Exception as e:
            contact_logger.error("Logging failed: %s", e)

            flash("Сталась помилка при обробленні даних", "danger")

        return redirect(url_for('contacts'))
        
    return render_template('contacts.html', form=form)

from .users import users_bp
from .products import products_bp
app.register_blueprint(users_bp)
app.register_blueprint(products_bp)