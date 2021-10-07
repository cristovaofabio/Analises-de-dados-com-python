from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

from flask import render_template
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)
