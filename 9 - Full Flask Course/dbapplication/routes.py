from flask import render_template, request, redirect, url_for, jsonify
from models import Person

def register_routes(app, db):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == "GET": 
            people = Person.query.all()
            return render_template('index.html', people=people)
        else:
            name = request.form['name']
            age = int(request.form['age'])
            job = request.form['job']
            person = Person(name=name, age=age, job=job) # type: ignore
            db.session.add(person)
            db.session.commit()

            return redirect(url_for('index'))
        
    @app.route('/delete/<pid>', methods=['DELETE'])
    def delete(pid):
        Person.query.filter_by(pid=pid).delete()
        db.session.commit()
        return jsonify({'success': True})
    
    @app.route('/details/<pid>')
    def details(pid):
        person = Person.query.filter(Person.pid == pid).first()
        return render_template('details.html', person=person)