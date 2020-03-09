from flask import Flask, render_template, request, redirect, session
from flask_session import Session
import redis

app = Flask(__name__)
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)

session['notes'] = []

@app.route("/")
def index():
    return render_template("index.html", notes=session['notes'])

@app.route("/add", methods=["GET", "POST"])
def add():
    note = request.form.get('new_note')
    session['notes'].append(note)
    return redirect("/")

@app.route("/remove", methods=["GET", "POST"])
def remove():
    for note in session['notes']:
        if note == request.form.get('delete_note'):
            session['notes'].remove(note)
    return redirect("/")
