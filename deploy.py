from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
title = "My ToDo List"

def get_notes():
    notes = []
    with open('todo.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            notes.append(row[0])
    return notes

def delete_note(d_note):
    updated = []
    with open('todo.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] != d_note:
                updated.append(row[0])
    save_notes(updated)
    return

def save_notes(notes):
    with open('todo.csv', mode='w') as update_file:
        for note in notes:
            note_writer = csv.writer(update_file)
            note_writer.writerow([note])
    return

def append_note(note):
    with open('todo.csv', mode='a') as update_file:
        note_writer = csv.writer(update_file)
        note_writer.writerow([note])
    return

def note_exists(note):
    with open('todo.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == note:
                return True
    return False

@app.route("/")
def index():
    notes = get_notes()
    total = len(notes)
    return render_template("index.html", notes=notes, edit=False, total=total, title=title)

@app.route("/add", methods=["GET", "POST"])
def add():
    new_note = request.form.get('new_note')
    notes = get_notes()
    if note_exists(new_note):
        total = len(notes)
        return render_template("index.html", notes=notes, edit=False, total=total, title="Already Added")
    append_note(new_note)
    notes.append(new_note)
    total = len(notes)
    return render_template("index.html", notes=notes, edit=False, total=total, title="Added")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    toEdit = request.form.get('before_note')
    notes = get_notes()
    total = len(notes)
    return render_template("index.html", notes=notes, edit=True, toEdit=toEdit, total=total, title=title)

@app.route("/edited", methods=["GET", "POST"])
def edited():
    if note_exists(request.form.get('after_note')):
        notes = get_notes()
        total = len(notes)
        return render_template("index.html", notes=notes, edit=False, total=total, title="Already Added")
    delete_note(request.form.get('before_note'))
    append_note(request.form.get('after_note'))
    return redirect("/")

@app.route("/remove", methods=["GET", "POST"])
def remove():
    delete_note(request.form.get('to_delete'))
    notes = get_notes()
    total = len(notes)
    return render_template("index.html", notes=notes, edit=False, total=total, title="Deleted")
