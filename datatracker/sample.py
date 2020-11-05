from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint

bp = Blueprint('sample', __name__)


@bp.route('/test')
def test():
    return "All good!"


@bp.route('/sample')
def index():
    message = "This text is coming from the 'sample.py' module, not the html file!"
    phrase = "Python is cool!"
    return render_template('sample/index.html', message=message, word=phrase)