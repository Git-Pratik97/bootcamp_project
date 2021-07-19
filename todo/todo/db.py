import datetime 
import random
import sqlite3

import click  #For creating beautiful command line interfaces 
from flask import current_app, g # g is for temporary data storage while app is running.
from flask.cli import with_appcontext # Commands with application context

from faker import Faker

def get_db():
	dbname = current_app.config['DATABASE'] 
	g.db = sqlite3.connect(dbname)
	g.db.execute("PRAGMA foreign_keys = ON;")
    return g.db
