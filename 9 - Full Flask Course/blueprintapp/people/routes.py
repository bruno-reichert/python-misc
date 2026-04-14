from flask import render_template, redirect, request, request, url_for, Blueprint
from blueprintapp import people
from blueprintapp.app import db
from blueprintapp.people.models import Person

people = Blueprint('people', __name__, template_folder='templates')

@people.route('/')
def index():
    people = Person.query.all()
    return render_template('people/index.html', people=people)

@people.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template('people/create.html')
    else:
        name = request.form.get('name')
        age = int(request.form.get('age')) # type: ignore
        job = request.form.get('job')
        job = job if job != '' else None
        person = Person(name=name, age=age, job=job) # type: ignore
        db.session.add(person)
        db.session.commit()
        return redirect(url_for('people.index')) 
      