from flask import Flask,render_template , request ,redirect ,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from requests import options

DB_NAME = "site.db"

app: Flask = Flask(__name__)
app.config["SECRET_KEY"] = "ıukhhgkjjgh"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
db = SQLAlchemy(app)
app.app_context().push()

@app.route("/")
def home():
    return render_template("index.html")

    
if __name__ == "__main__":
    app.debug = False
    app.run(host="0.0.0.0")