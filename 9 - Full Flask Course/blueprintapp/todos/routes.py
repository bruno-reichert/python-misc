from flask import render_template, redirect, request, request, url_for, Blueprint
from blueprintapp.app import db
from blueprintapp.todos.models import Todo

todos = Blueprint('todos', __name__, template_folder='templates')

@todos.route('/')
def index():
    todos = Todo.query.all()
    return render_template('todos/index.html', todos=todos)

@todos.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template('todos/create.html')
    else:
        title = request.form.get('title')
        description = request.form.get('description')
        done = True if 'done' in request.form.keys() else False
        description = description if description != '' else None
        todo = Todo(title=title, description=description, done=done) # type: ignore
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('todos.index'))