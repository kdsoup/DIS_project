from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import numpy as np
import pandas as pd
from sqlalchemy import text

app = Flask(__name__ , static_url_path='/static')
app.config['SECRET_KEY'] = 'your_secret_key'

# Please set port address and database name below
# 'postgresql://postgres@localhost:XXXX/XXXX'
# e.g 'postgresql://postgres@localhost:5432/winey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:XXXX/XXXX'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class Wine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100000))
    designation = db.Column(db.String(100))
    points = db.Column(db.Float)
    price = db.Column(db.Float)
    province = db.Column(db.String(100))
    region_1 = db.Column(db.String(100))
    region_2 = db.Column(db.String(100))
    variety = db.Column(db.String(100))
    winery = db.Column(db.String(100))

# Routes
@app.route("/", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        #Check if user already exists in DataBase
        user_check_query = text('select * from "user" where "username" = :username')
        # Fetchone returns either a single row or None if no rows exist
        user_check = db.session.execute(user_check_query, {'username': username}).fetchone()
        #check specific users password
        password_check_query = text('select * from "user" where "username" = :username and "password" = :password')
        password_check = db.session.execute(password_check_query, {'username': username, 'password': password}).fetchone()
        if user_check == None:
            user_insert_query = text('insert into "user" ("username", "password") values (:username, :password)')
            db.session.execute(user_insert_query, {'username': username, 'password': password})
            db.session.commit()
            flash('acc created', ' success')
            return redirect(url_for('home'))
        elif user_check != None and password_check != None:
            flash('Welcome back', 'success')
            return redirect(url_for('home'))
        else:
            flash('username or password is incorrect', 'danger')
    return render_template('register.html')

@app.route("/home")
def home():
    wines = Wine.query.all()
    if request.method == 'POST':
        with db.engine.connect() as conn:
          search_re = request.form['search']
          search_option = request.form['option']
          print(search_option)
          sql = text(f"select * from wine where {search_option} ~* '{search_re}' ") # case-insensitive sql regex query
          search_results = conn.execute(sql)
        return render_template('home.html', wines=search_results)
    return render_template('home.html', wines=wines)

@app.route("/wines")
def wines():
    wines = Wine.query.all()
    return render_template('wines.html', wines=wines)

@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        with db.engine.connect() as conn:
          search_re = request.form['search']
          search_option = request.form['option']
          print(search_option)
          sql = text(f"select * from wine where {search_option} ~* '{search_re}' ") # case-insensitive sql regex query
          search_results = conn.execute(sql)
        return render_template('search_results.html', wines=search_results)
    return render_template('search.html')

# Load CSV data into the database
def load_wine_data():
    if not Wine.query.first():
        df = pd.read_csv('winedata_50.csv')
        df.columns = ['index', 'country', 'description', 'designation', 'points', 'price', 'province', 'region_1', 'region_2', 'variety', 'winery']

        
        df['points'] = pd.to_numeric(df['points'], errors='coerce')
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df = df.replace({np.nan: None}) 

        for _, row in df.iterrows():
            wine = Wine(
                country=row['country'],
                description=row['description'],
                designation=row['designation'],
                points=row['points'],
                price=row['price'],
                province=row['province'],
                region_1=row['region_1'],
                region_2=row['region_2'],
                variety=row['variety'],
                winery=row['winery']
            )
            db.session.add(wine)
        db.session.commit()
@app.before_request
def before_request():
    load_wine_data()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
