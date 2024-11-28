from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)
app.secret_key = 'SDA'


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)





@app.route('/')
def home():
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)