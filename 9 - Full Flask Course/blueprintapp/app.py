from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./blueprints.db'

    db.init_app(app)

    from blueprintapp.todos.routes import todos
    from blueprintapp.people.routes import people
    from blueprintapp.core.routes import core
    app.register_blueprint(todos, url_prefix='/todos')
    app.register_blueprint(people, url_prefix='/people')
    app.register_blueprint(core)

    migrate = Migrate(app, db) 
    return app