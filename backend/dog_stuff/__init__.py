from flask import Flask

def create_app():
	app = Flask(__name__, instance_relative_config=True)
  
	from . import dogs, invoices
	app.register_blueprint(dogs.bp)
	app.register_blueprint(invoices.bp)

	return app