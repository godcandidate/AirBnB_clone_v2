#!/usr/bin/python3
"""this script that starts a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """this handles the root url"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """this handles hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """this handles /c/<text> route"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """this handles /python/<text> route"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """this handles /number/<n> route"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """this handles /number_template/<int:n> route"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """this handles /number_template/<int:n> route"""
    parity = 'odd'
    if n % 2 == 0:
        parity = 'even'
    return render_template('6-number_odd_or_even.html', n=n, parity=parity)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
