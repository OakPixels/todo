from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def index():
    notes = []
    with open('todo.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            notes.append(row[0])
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["GET", "POST"])
def add():
    note = request.form.get('new_note')
    with open('todo.csv', mode='a') as todo_file:
        note_writer = csv.writer(todo_file)
        note_writer.writerow([note],)
    return redirect("/")

@app.route("/remove", methods=["GET", "POST"])
def remove():
    updated = []
    with open('todo.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row[0])
            print(request.form.get('delete_note'))
            print('...')
            print(row[0] == request.form.get('delete_note'))
            if row[0] != request.form.get('delete_note'):
                updated.append(row[0])
    with open('todo.csv', mode='w') as update_file:
        for note in updated:
            note_writer = csv.writer(update_file)
            note_writer.writerow([note])
    return redirect("/")
