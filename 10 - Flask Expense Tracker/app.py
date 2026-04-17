from flask import Flask, render_template, request, redirect, url_for, make_response, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime, date

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a random secret key in production
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False, default=date.today())


@app.route('/')
def index():
    expenses = Expense.query.order_by(Expense.date.desc(), Expense.id.desc()).all()
    print(expenses)
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add():
    description = (request.form.get('description') or "").strip()
    amount_str = (request.form.get('amount') or "").strip()
    category = (request.form.get('category') or "").strip()
    date_str = (request.form.get('date') or "").strip()
    
    if not description or not amount_str or not category or not date_str:
        flash("All fields are required.", "error")
        return redirect(url_for('index'))
    try:
        amount = float(amount_str)
        if amount <= 0:
            raise ValueError
    except ValueError:
        flash("Amount must be a positive number.", "error")
        return redirect(url_for('index'))
    
    try:
        d = datetime.strptime(date_str, '%Y-%m-%d').date() if date_str else date.today()
    except ValueError:
        d = date.today()

    e = Expense(description=description, amount=amount, category=category, date=d) # type: ignore
    db.session.add(e)
    db.session.commit()
    flash("Expense added successfully!", "success")
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True, port=4848)