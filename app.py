from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	headline = "PYTHON AGGRESSIVE"
	return render_template ("python.html", headline=headline)

@app.route("/cornelius")
def cornelius():
	headline = "PYTHON CORNELIUS"
	return render_template ("python.html", headline=headline)

