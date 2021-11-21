from flask import Flask, request, jsonify, url_for, render_template
import os
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('Login.html')


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT','8069')),
        debug=True)