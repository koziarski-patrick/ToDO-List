from flask import (render_template, flash, redirect,
                   url_for, request, Blueprint)
from flask_login import current_user, login_user, logout_user
from app import db
from app.models import User
from app.users.forms import (RegistrationForm, LoginForm)
from werkzeug.urls import url_parse

users = Blueprint('users', __name__)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password!', category='danger')
            return redirect(url_for('users.login'))
        login_user(user, remember=form.remember.data)
        flash('You have been logged in!', category='success')
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.home')
        return redirect(next_page)
    return render_template('login.html', title='ToDo - Login', form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', category='success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='ToDo - Register', form=form)
