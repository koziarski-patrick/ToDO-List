from flask import render_template, Blueprint
from flask_login import login_required, current_user
from app.models import Todo

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html', title='ToDo', user=current_user)
