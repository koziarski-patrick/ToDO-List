from flask import (redirect, url_for, request, jsonify, Blueprint)
from flask_login import current_user
from app import db
from app.models import Todo
from datetime import datetime

posts = Blueprint('posts', __name__)


@posts.route("/insert", methods=['POST'])
def insert():
    data = request.get_json()
    if request.method == 'POST':
        if (len(data['date']) != 0):
            new_date = date(data['date'])
            insert_data = Todo(
                task=data['description'], status='In Progress', user_id=current_user.id, date=new_date)
            db.session.add(insert_data)
            db.session.commit()
        else:
            insert_data = Todo(
                task=data['description'], status='In Progress', user_id=current_user.id)
            db.session.add(insert_data)
            db.session.commit()
        result = {'success': True, 'response': 'Task added successfully!'}
    else:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)


@posts.route("/remove/<int:id>", methods=['POST'])
def remove(id):
    remove_data = request.get_json()
    if request.method == 'POST' and id == remove_data['ID']:
        remove = Todo.query.get_or_404(remove_data['ID'])
        db.session.delete(remove)
        db.session.commit()
        result = {'success': True, 'response': 'Record deleted successfully!'}
    else:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)


@posts.route("/update/<int:id>", methods=['POST'])
def update(id):
    if request.method == 'POST':
        update_data = Todo.query.get_or_404(id)
        update_data.task = request.form['eText']
        if (len(request.form['eDate']) != 0):
            new_date = date(request.form['eDate'])
            update_data.date = new_date
        else:
            update_data.date = None
        db.session.commit()
        return redirect(url_for('main.home'))
    else:
        return redirect(url_for('main.home'))


@posts.route("/status/<int:id>", methods=['POST'])
def edit(id):
    update_status = request.get_json()
    try:
        update_data = Todo.query.get_or_404(id)
        if "status" in update_status:
            update_data.status = update_status['status']
            result = {'success': True, 'response': 'Status Updated'}
            db.session.commit()
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)

# Convert and format date string to date object
def date(date):
    expiration_year = int(date[:4])
    expiration_month = int(date[5:7])
    expiration_date = int(date[8:10])
    expiration_date = datetime(
        expiration_year, expiration_month, expiration_date)
    return expiration_date
