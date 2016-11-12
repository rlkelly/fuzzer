import flask
from flask import Flask, request

from werkzeug.exceptions import BadRequest

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] == 'ROB' and request.form['password'] == 's3cREt!':
        return flask.jsonify(**{'success': True})
    else:
        return BadRequest('Invalid Login')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
