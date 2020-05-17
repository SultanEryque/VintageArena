from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Wake Cornelius"

@app.route("/<string:name>")
def wake(name):
	name = name.capitalize()
	return f"<h1>wake {name}</h1>"
