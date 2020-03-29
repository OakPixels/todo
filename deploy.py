from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

def get_notes():
    notes = []
    with open('todo.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            notes.append(row[0])
    return notes

def remove_notes(d_note):
    updated = []
    with open('todo.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row[0])
            if row[0] != d_note:
                updated.append(row[0])
    return updated

def save_notes(notes):
    with open('todo.csv', mode='w') as update_file:
        for note in notes:
            note_writer = csv.writer(update_file)
            note_writer.writerow([note])
    return

@app.route("/")
def index():
    notes = get_notes()
    return render_template("index.html", notes=notes, edit=False)

@app.route("/add", methods=["GET", "POST"])
def add():
    note = request.form.get('new_note')
    with open('todo.csv', mode='a') as todo_file:
        note_writer = csv.writer(todo_file)
        note_writer.writerow([note],)
    return redirect("/")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    notes = get_notes()
    return render_template("index.html", notes=notes, edit=True)

@app.route("/edited", methods=["GET", "POST"])
def edited():
    note = request.form.get('before_note')
    updated = []
    with open('todo.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] != request.form.get('before_note'):
                updated.append(row[0])
            else:
                updated.append(request.form.get('after_note'))
    #When edit button pressed create update list with new note edited
    save_notes(updated)
    return redirect("/")

@app.route("/remove", methods=["GET", "POST"])
def remove():
    updated = remove_notes(request.form.get('delete_note'))
    print(updated)
    save_notes(updated)
    return redirect("/")
