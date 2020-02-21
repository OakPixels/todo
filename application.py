from flask import Flask, render_template, request, redirect, session
from flask_session.__init__ import Session

app = Flask(__name__)

SESSION_PERMANENT = False
SESSION_TYPE = "filesystem"
Session(app)

notes = []

@app.route("/")
def index():
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["GET", "POST"])
def add():
    notes.append(request.form.get("new_note"))
    return redirect("/")

@app.route("/remove", methods=["GET", "POST"])
def remove():
    notes.remove(request.form.get("delete_note"))
    return redirect("/")
