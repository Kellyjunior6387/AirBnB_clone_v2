#!/usr/bin/python3
"""
Start a Flask appliction
"""


from flask import Flask, render_template
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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def PythonText(text):
    return 'Python {}'.format(escape(text).replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def displaynumber(n):
    if n.isdigit():
        return '{} is a number'.format(escape(n))
    else:
        abort(404)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if n.isdigit():
        return render_template('5-number.html', n=n)
    else:
        abort(404)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddoreven(n):
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
