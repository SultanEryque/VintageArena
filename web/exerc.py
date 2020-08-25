from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def project1():
    return render_template("pgmExplanation.html")

