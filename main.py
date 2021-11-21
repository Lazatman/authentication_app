from flask import Flask, request, jsonify, render_template
from flask_login import LoginManager
import os
from models import users
from models import db_connect
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('Login.html')
    elif request.form['email'] and request.form['mdp']:
        return jsonify(
            {
                "status": 200,
                "result": 'Success!',
                "email": request.form['email'],
                "mdp": request.form['mdp']
            })
    else:
        return jsonify(
            {
                "status": 400,
                "result": 'Fail!'
            })


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT', '8069')),
        debug=True)
