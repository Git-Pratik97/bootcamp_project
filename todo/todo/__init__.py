import os 
import random

from flask import Flask, render_template

def create_app():
	app = Flask("todo")
	
	app.config.from_mapping(
		DATABASE = os.path.join(app.instance_path, 'todo.sqlite')
	)
	
	if test.config is not None:
		app.config.update(test_config)
		
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass
		
	from . import todo
	app.register_blueprint(todo.bp) # Extends the content of application 
	
	from . import db
	db.init_app(app) #Safely bind database handler with app

