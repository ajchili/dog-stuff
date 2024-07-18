from flask import Blueprint, request
from json import loads

bp = Blueprint('dogs', __name__, url_prefix='/dogs')

dogs = []

@bp.route("/", methods=["GET", "POST"])
def dogs_handler():
	if request.method == "GET":
		return dogs
	
	request_data = loads(request.data)

	if "name" not in request_data:
		return "Name not provided"
	
	name = request_data["name"]

	dogs.append({ "name": name })
	return f"Welcome {name} to the pack!"

@bp.route("/<name>", methods=["GET", "PATCH", "DELETE"])
def dog_handler(name):
	dog = next(filter(lambda dog: dog["name"] == name, dogs), None)

	if dog is None:
		return "No dog with that name found!"
	
	if request.method == "GET":
		return dog
	
	return "not yet implemented :("