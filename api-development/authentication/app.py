
from flask import Flask,request,url_for,render_template
from sqlalchemy.dialects.mysql.base import colspecs
from flask_migrate import Migrate, migrate

# Settings for migrations
migrate = Migrate(app, db
app = Flask(__name__)
app.debug = True

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

class Profile(db.Model):
    # Id : Field which stores unique id for every row in
    # database table.
    # first_name: Used to store the first name if the user
    # last_name: Used to store last name of the user
    # Age: Used to store the age of the user
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    zip = db.Column(db.Integer(20), nullable=False)
    state = db.Column(db.String(20), nullable=False)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/add" methods=["POST"])
def add():
    first_name =request.form.get("")
    last_name = request.form.get("")
    first_name = request.form.get("")
    first_name = request.form.get("")
    first_name = request.form.get("")
    first_name = request.form.get("")


if __name__ =="main":
    app.run("debug=True")