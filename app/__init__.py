from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


# Init Flask application
app = Flask(__name__)
app.config.from_object('config')

# Init database with SQLAlchemy
db = SQLAlchemy(app)

# Set error handlers
# TODO: Add 500, 400, etc.
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Register blueprints
# TODO: Create blueprints and register over here
from app.address.controllers import address_page
from app.report.controllers import report_page 

app.register_blueprint(address_page)
app.register_blueprint(report_page)


# Setup database
db.create_all()

