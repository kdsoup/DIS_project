# Winey

This is the application called *Winey* for the DIS project. 
We have used a small sample of the [Wine Reviews](https://www.kaggle.com/datasets/zynicide/wine-reviews) dataset on Kaggle.

Users of Winey can signup and login to the Winey app and seach for wines using the wine descriptions or province names.

## Documentation
How to compile and run the project can be found below in this ```README``` file.

The E/R diagram can be found in the folder ```diagram```.
## Webapp
Our webapp interracts with the database using SQL in line 45, 49 and 52 in the ```app.py``` file.

Regular expression is use in the search function on line 67-75 in the ```app.py``` file.

# Install Requirements

To install the package requirements for the Winey app in a miniconda enviroment, use the following command:

```bash
conda create -y -n "winey" python=3.12
conda activate winey
pip install -r requirements.txt
```

# Setup Database

1) Start Postgres server and make a new database with the name ```winey```. 

2) To connect correctly to the database, please add your local port and database name to line 14. 
For example if your port is 5432 and database name is 'winey' then edit

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:XXXX/XXXX'
```

to the follwing:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/winey'
```

3) In the terminal, go to the folder ```/Winey/src``` and type the commands:

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

# Run App

To run the app (in the miniconda env) use the command:

```bash
python3 Winey/src/app.py
```


