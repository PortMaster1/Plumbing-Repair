import sys, os, requests
from flask import Flask, request, jsonify, render_template, redirect, url_for

from userlist_generator import Generate, Reissue

app = Flask(__name__)
UPLOAD_FOLDER = "."
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

g = Generate()
r = Reissue()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part in the request.', 400

    file = request.files['file']
    if file.filename == '':
        return 'No file selected.', 400

    file.save(os.path.join(app.config['UPLOAD_FOLDER'], "users.txt"))
    g.generate()
    return f"File '{file.filename}' uploaded successfully!"

if __name__ == '__main__':
    app.run(debug=True)