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

CATEGORIES = ['Food', 'Transport', 'Rent', 'Utilities', 'Health']

def parse_date_or_none(s:str):
    if not s:
        return None
    try:
        return datetime.strptime(s, '%Y-%m-%d').date() 
    except ValueError:
        return None

@app.route('/')
def index():
    start_str = (request.args.get('start') or "").strip()
    end_str = (request.args.get('end') or "").strip()

    start_date = parse_date_or_none(start_str)
    end_date = parse_date_or_none(end_str)

    if start_date and end_date and start_date > end_date:
        flash("Start date cannot be after end date.", "error")
        start_date = end_date = None
        start_str = end_str = ""

    q = Expense.query
    if start_date:
        q = q.filter(Expense.date >= start_date)
    if end_date:
        q = q.filter(Expense.date <= end_date)

    expenses = q.order_by(Expense.date.desc(), Expense.id.desc()).all()
    total = round(sum(e.amount for e in expenses), 2)
    print(expenses)
    return render_template(
        'index.html', 
        expenses=expenses, 
        categories=CATEGORIES, 
        total=total,
        start_str = start_str,
        end_str = end_str,
        today = date.today().isoformat()
        )

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

@app.route('/delete/<int:expense_id>', methods=['POST'])
def delete(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    db.session.delete(expense)
    db.session.commit()
    flash("Expense deleted successfully!", "success")
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True, port=4848)