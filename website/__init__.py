from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"
def create_app():
    #Creating new App
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Simple Secret Key"

    ## Adding database to the application
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Adding routes
    from.routes import routes  # Import the routes module from the routes.py file
    # Register the routes Blueprint with the Flask app, using the URL prefix "/". This means that all routes defined in the routes.py file will be accessible at the "/<prefix>" URL. For example, if the prefix is "/courses", the routes defined in the routes.py file will be accessible at "/courses/<route>".

    # Registering the routes Blueprint with the Flask app. The URL prefix "/courses" is used to specify that all routes defined in the routes.py file will be accessible at the "/courses" URL. For example, if the routes defined in the routes.py file are "/courses/view", "/courses/add", etc., they will be accessible at "/courses/view", "/courses/add", etc
    app.register_blueprint(routes, url_prefix="/")

    #Creating Database
    create_database(app)
    return app
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():  # Use the application context
            db.create_all()
        print("Database Created")
