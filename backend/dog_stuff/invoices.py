from flask import Blueprint, request
from PIL import Image
from pytesseract import image_to_string

bp = Blueprint('invoices', __name__, url_prefix='/invoices')

@bp.route("/upload", methods=["POST"])
def file_upload_handler():
    data = dict()

    files = request.files.getlist("images")

    for file in files:
        img = Image.open(file)
        data[file.filename] = image_to_string(img)

    return data