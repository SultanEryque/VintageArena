from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def python():
	return render_template("python.html")

@app.route("/venom", methods=["POST"])
def venom():
	name = request.form.get("name")
	return render_template("venom.html", name=name)

