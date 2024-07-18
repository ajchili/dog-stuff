from flask import Flask, request
from PIL import Image
from pytesseract import image_to_string

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/upload", methods=["POST"])
def file_upload_handler():
    data = dict()

    files = request.files.getlist("images")

    for file in files:
        img = Image.open(file)
        data[file.filename] = image_to_string(img)

    return data
