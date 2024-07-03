import random
from flask import Flask, jsonify, redirect, render_template, request
import sqlalchemy
from . import models

app = Flask(__name__)
app.config.from_object('config')


@app.route("/")
def index():
    try:
        tasks = models.Task.query.order_by(models.Task.created_at)
        return render_template("index.html", tasks = tasks)
    except(sqlalchemy.exc.OperationalError):
        return render_template("index.html")

@app.route("/add/", methods=['POST'])
def add_task():
    
    try:
        name = request.form['task']
        description = request.form['description']
        if not description == '':
            models.db.session.add(models.Task(name, description))
        elif name == '':
            return redirect("/")
        else:
            description = "no description"
            models.db.session.add(models.Task(name, description))
        models.db.session.commit()  
        return redirect("/")
    except(Exception):
        return redirect("/")

@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    try:
        task = models.Task.query.get_or_404(id)
        new_name = request.form['task']
        new_description = request.form['description']
        if not new_description == '':
            task.name = new_name
            task.short_description = new_description
        else:
            new_description = "no description"
            task.name = new_name
            task.short_description = new_description 
        models.db.session.add(task)   
        models.db.session.commit()    
        return redirect("/")
    except(sqlalchemy.exc.ArgumentError):
        return redirect("/")

@app.route("/modif/<int:id>")
def modif_route(id):
    return render_template("update.html", id = id)


@app.route("/delete/<int:id>")
def test(id):
    try:
        task = models.Task.query.get_or_404(id)
        models.db.session.delete(task)
        models.db.session.commit()
        return redirect("/")
    except(sqlalchemy.exc.ArgumentError):
        return redirect("/")
    

@app.errorhandler(404)
def page_not_found(e):
    page_404_list = ["404_page1.html", "404_page2.html", "404_page3.html", "404_page4.html", "404_page5.html", "404_page6.html"]
    page_choice = random.sample(page_404_list, 1)
    return render_template(page_choice)