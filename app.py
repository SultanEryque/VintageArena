import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def python():
	names = ["Cornelius", "Samaritan", "Root"]
	return render_template("python.html", names=names)

@app.route("/venom")
def venom():
	now = datetime.datetime.now()
	venom = now.month == 3 and now.day == 17
	return render_template("venom.html", venom=venom)

