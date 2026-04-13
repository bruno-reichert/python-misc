from flask import render_template, request, redirect, url_for, jsonify
from models import User
from flask_login import login_user, logout_user, current_user, login_required


def register_routes(app, db, bcrypt):
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == "GET":
            return render_template('signup.html')
        else:
            username = request.form.get('username')
            password = request.form.get('password')
            hashed_password = bcrypt.generate_password_hash(password)
            user = User(username=username, password=hashed_password) # type: ignore
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        
    @app.route('/login/', methods=['GET', 'POST'])
    def login():
        if request.method == "GET":
            return render_template('login.html')
        else:
            username = request.form.get('username')
            password = request.form.get('password')

            user = User.query.filter_by(username=username).first()
            if bcrypt.check_password_hash(user.password, password): # type: ignore
                login_user(user)
                return redirect(url_for('index'))
            else:
                return 'Failed'
            
    
    @app.route('/logout', methods=['GET', 'POST'])
    def logout():
        logout_user()
        return redirect(url_for('index'))
    
    @app.route('/secret')
    @login_required
    def secret():
        return 'This is a secret page!'