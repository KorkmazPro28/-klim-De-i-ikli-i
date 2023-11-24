## Projemin türü:
> iklim değişikliği ile ilgili site

## Kullanacağım kütüphaneler:
- Flask
- Flask_SQLalchemy
- Requests

## İşe yarayabilecek referanslar:
- Elimde işime yarayacak bir sürü kod var.

- Bir tanesi :

from flask import Flask , render_template , request ,redirect ,url_for,flash
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from requests import options
import tkinter as tk
import ctypes  # An included library with Python install.

DB_NAME = "site.db"

app: Flask = Flask(__name__)
app.config["SECRET_KEY"] = "ıukhhgkjjgh"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
db = SQLAlchemy(app)
app.app_context().push()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    dreams = db.relationship("Dreams", backref="dreamer")

class Dreams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dream = db.Column(db.String(300), nullable=False)
    deta = db.Column(db.Text)
    de = db.Column(db.String(300), nullable=False)
    date_added = db.Column(db.DateTime, default = datetime.utcnow)
    dreamer_id = db.Column(db.Integer, db.ForeignKey("users.id"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register" , methods=["GET" , "POST"])
def register():
    
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        email = request.form.get("email")
        password = request.form.get("password")

        search = Users.query.filter_by(email=email).first()

        if search != None:
            flash("Bu E-Posta İle Hesap Zaten Bulunuyor !!!")
            return render_template("register.html")
        new_user = Users(name = name,surname = surname,email = email,password=password)
        db.session.add(new_user)
        db.session.commit()          
        ctypes.windll.user32.MessageBoxW(None, "Kaydolma İşleminiz Başarıyla Tamamlndı Giriş Yap Sayfasına Yönlendiriliyorsunuz ...", "Uyarı", 0x00000000)
    
    


        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/detail")
def detail():
    return render_template("detail.html")

@app.errorhandler(404)
def eror(e):
    return render_template("404.html")

if __name__ == "__main__":


    app.debug = False
    app.run(host="0.0.0.0")


## Geliştirme sırasında bana yardımcı olabilecek kılavuz kaynaklar
Yukarıda yazdığım kod
