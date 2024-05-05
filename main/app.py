from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/datastore.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # Initialize SQLAlchemy

# Define your database models using SQLAlchemy's declarative syntax
class Users(db.Model):
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/<username>')
def hello_user(username):
    user = Users.query.filter_by(username=username).first()
    if user is None:
        return 'User not found!'
    return 'Hello, ' + str(username) + ' !'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')