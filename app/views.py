from flask import render_template, request, Blueprint

main = Blueprint("main", __name__)

@main.route('/')
def index():
    return "index page", 200

@main.route('/homepage') 
def home():
    """View for the Home page of your website."""
    user_agent = str(request.user_agent)[:10]
    return render_template("base.html", agent=user_agent)