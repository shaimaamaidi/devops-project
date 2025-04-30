from flask import Blueprint, render_template
from services.logic import get_message

main = Blueprint('main', __name__)

@main.route('/')
def home():
    message = get_message()
    return render_template('index.html', message=message)
