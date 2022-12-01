from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    tasks = db.relationship('Todo', backref='todo', lazy='dynamic')

    # Hash Password
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    #  String Representation
    def __repr__(self):
        return '<ID: {}, USERNAME: {}, EMAIL: {}, PASSWORD: {}>'.format(self.id, self.username, self.email, self.password)

# Todo Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(200))
    date = db.Column(db.DateTime, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    #  String Representation
    def __repr__(self):
        return '<ID: {}, TASK: {}, STATUS: {}, DATE: {}>'.format(self.id, self.task, self.status, self.date)
