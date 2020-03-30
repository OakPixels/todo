from flask import Flask, session, render_template, request, redirect
import csv

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# Render webpage
def page(notify, edit, toEdit):
    notes = session['notes']
    total = len(notes)
    if notify != None:
        title = notify
    else:
        title = session['username'] + "'s " + "ToDo List"
    if edit == True:
        return render_template("index.html", notes=notes, edit=True, toEdit=toEdit, total=total, title=title)
    else:
        return render_template("index.html", notes=notes, edit=False, total=total, title=title)


# URL Routes
@app.route("/")
def index():
    if 'username' in session:
        if 'notes' not in session:
            session['notes'] = []
        return page(None, False, None)
    return redirect('/login')

@app.route("/login", methods=["GET", "POST"])
def login():
    # If logged in go to homepage
    if 'username' in session:
        return redirect('/')
    if request.method == 'POST':
        session['username'] = request.form.get('name').capitalize()
        return redirect('/')
    return render_template("login.html", title="Welcome")

@app.route("/add", methods=["GET", "POST"])
def add():
    new_note = request.form.get('new_note')
    notes = session['notes']
    for note in notes:
        if new_note == note:
            total = len(notes)
            return render_template("index.html", notes=notes, edit=False, total=total, title="Already Added")
    notes.append(new_note)
    session['notes'] = notes
    notify = "Added"
    return page(notify, False, None)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    toEdit = request.form.get('before_note')
    return page(None, True, toEdit)

@app.route("/edited", methods=["GET", "POST"])
def edited():
    notes = session['notes']
    for note in notes:
        if (note == request.form.get('after_note')):
            notify = "Already Added"
            return page(notify, False, None)
    notes.remove(request.form.get('before_note'))
    notes.append(request.form.get('after_note'))
    session['notes'] = notes
    return redirect('/')

@app.route("/remove", methods=["GET", "POST"])
def remove():
    notes = session['notes']
    notes.remove(request.form.get('to_delete'))
    session['notes'] = notes
    notify = "Deleted"
    return page(notify, False, None)

@app.route("/logout", methods=["GET", "POST"])
def logout():
    notify = "Logged out"
    session.pop('username', None)
    session.pop('notes', None)
    return render_template("login.html", title=notify)
