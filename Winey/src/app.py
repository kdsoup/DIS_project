from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
import numpy as np
import pandas as pd
import psycopg2

app = Flask(__name__ , static_url_path='/static')
db = "dbname='postgres' user='postgres' host='127.0.0.1' password = '  '"
conn = psycopg2.connect(db)
cursor = conn.cursor()
# app.config['SECRET_KEY'] = 'your_secret_key'

# Please set localhost address and server name below
# 'postgresql://postgres@localhost:XXXX/XXXX'
# e.g 'postgresql://postgres@localhost:5432/winey'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/wineyDB'
db = SQLAlchemy(app)
# migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
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
    cur = conn.cursor()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur.execute(f'''select * from users where username = '{username}' ''')
        existing_user = cur.fetchone()
        if existing_user:
            if existing_user[2] == password:  # Assuming password is at index 2 in the tuple
                flash('Welcome Back gamle dreng', 'success')
                return redirect(url_for('home'))
            else:
                flash('Invalid password', 'danger')
        else:
            cur.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
            conn.commit()
            flash('Your account has been created!', 'success')
            return redirect(url_for('home'))
        return render_template('register.html')
        # if not User.query.filter_by(username=username).first():
        #     db.engine.execute("INSERT INTO user (username, password) VALUES (:username, :password)", 
        #                       {'username': username, 'password': password})    
        #     # user = User(username=username, password=password)
        #     # db.session.add(user)
        #     # db.session.commit()
        #     flash('Your account has been created!', 'success')
        #     return redirect(url_for('home'))
        # elif User.query.filter_by(username=username).first() and User.query.filter_by(password=password).first():
        #     flash('Welcome Back gamle dreng', 'success')
        #     return redirect(url_for('home'))
        # else:
        #     flash('Username username or password doesnt exist', 'danger')
        # return redirect(url_for('register'))
    

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/wines")
def wines():
    wines = Wine.query.all()
    return render_template('wines.html', wines=wines)

@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_string = request.form['search']
        search_results = Wine.query.filter(Wine.description.like(f'%{search_string}%')).all()
        return render_template('search_results.html', wines=search_results)
    return render_template('search.html')

# Load CSV data into the database
def load_wine_data():
    if not Wine.query.first():
        df = pd.read_csv('winetest.csv')
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
