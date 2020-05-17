import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def python():
	now = datetime.datetime.now()
	python_day = now.month == 5 and now.day == 17
	return render_template ("python.html", python_day=python_day) 
