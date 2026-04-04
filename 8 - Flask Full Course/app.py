# Imports
from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# My App
app = Flask(__name__)
Scss(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

# Data class - row of data
class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.now())

    def __str__(self) -> str:
        return f"Task {self.id}: {self.content}"

@app.route("/")
def index():
    return render_template("index.html")

# Runner and debugger
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)