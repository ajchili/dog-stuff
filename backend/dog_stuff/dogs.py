from flask import Blueprint

bp = Blueprint('dogs', __name__, url_prefix='/dogs')

@bp.route("/bork", methods=["GET"])
def file_upload_handler():
	return "bark"