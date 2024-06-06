# DIS_project

This is the application for Winey project.

# Install Requirements

To install the package requirements for the Winey app in a miniconda enviroment, use the following command:

```bash
conda create -y -n "winey" python=3.12
conda activate winey
pip install -r Winey/src/requirements.txt
```

# Setup app.py

To connect correctly to the database, please add your local port number and Postgres server name to line 13. 
For example if your port is 5432 and servername is 'winey' then edit

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:XXXX/XXXX'
```

to the follwing:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/winey'
```

# Setup Database

In PGAdmin make a new database with the name ```winey```. 

In the terminal, go to the folder ```./Winey/src``` and type the commands:

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

# Deliverable requirements
## Documentation
How to compile and run the project can be found above in this README file.

The E/R diagram can be found in the folder diagram.
## Webapp
Our webapp interracts with the database using SQL in line 45, 49 and 52 in the app.py file.

Regular expression is use in the search function on line 76-87 and 96-108 in the app.py file.
