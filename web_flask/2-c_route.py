#!/usr/bin/python3
"""
Start a flask application
"""


from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_bnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def Ctext(text):
    return 'C {}'.format(escape(text).replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
