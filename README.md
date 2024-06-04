# DIS_project

This is the application for Winey project.

# Install Requirements

To install the package requirements for the Winey app in a miniconda enviroment, use the following command:

```bash
conda create -y -n "winey" python=3.12
conda activate winey
pip install -r Winey/src/requirements.txt
```

# Setup Database

Go to the folder ```./Winey/src``` and type the commands:

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
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

# Run App

To run the app (in the miniconda env) use the command:

```bash
python3 Winey/src/app.py
```
