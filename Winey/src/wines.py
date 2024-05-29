from app import wines
from flask_login import UserMixin

class User(wines.Model, UserMixin):
    id = wines.Column(wines.Integer, primary_key=True)
    username = wines.Column(wines.String(20), unique=True, nullable=False)
    # email = wines.Column(wines.String(120), unique=True, nullable=False)
    password = wines.Column(wines.String(60), nullable=False)

class Wine(wines.Model):
    id = wines.Column(wines.Integer, primary_key=True)
    country = wines.Column(wines.String(100), nullable=True)
    description = wines.Column(wines.String(200), nullable=True)
    name = wines.Column(wines.String(100), nullable=True) #designation
    points = wines.Column(wines.Float, nullable=True)
    price = wines.Column(wines.Float, nullable=True)
    province = wines.Column(wines.String(100), nullable=True)
    region_1 = wines.Column(wines.String(100), nullable=True)
    region_2 = wines.Column(wines.String(100), nullable=True)
    variety = wines.Column(wines.String(100), nullable=True)
    winery = wines.Column(wines.String(100), nullable=True)




    # ,country,description,designation,points
    # ,price,province,region_1,region_2,variety,winery
