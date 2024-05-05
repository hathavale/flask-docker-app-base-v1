from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
database_dir = os.path.join(basedir, '..', 'db')
database_path = os.path.join(database_dir, '..', 'datastore.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/<username>')
def hello_user(username):
    return 'Hello, ' + username + ' !'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')