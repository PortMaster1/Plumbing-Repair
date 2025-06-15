import sys, os, requests, secrets
from flask import Flask, request, jsonify, render_template, redirect, url_for

# Relative imports
from userlist_generator import Generate, Reissue
import sql_connector

# Setup the web server
app = Flask(__name__)
UPLOAD_FOLDER = "."
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

g = Generate()
r = Reissue()

def update_clients(ip, _secret, shortname):
    subprocess.run(["sudo", "./update_clients", ip, _secret, shortname])

@app.route('/')
def index():
    return render_template('index.html', new=sql_connector.new_accounts)

@app.route('/manage')
def manage_accounts():
    if request.method == 'POST':
        print("Generating accounts...")
    users = g.all_accounts
    return render_template('manage.html', users=users)

@app.route('/reissue', methods=['POST'])
def reissue_account():
    username = request.form.get('username')
    if not username:
        return 'Username is required.', 400
    r.find_user(username)
    ppsk = r.replacr_ppsk(username)
    user = {"name": username, "ppsk": ppsk}
    return render_twmplate("reissued.html", user=user)

@app.route('/add_client')
def add_client():
    if request.method == 'POST':
        ip = request["ip_address"]
        _secret = request["secret"]
        shortname = request["shortname"]
        update_clients(ip, _secret, shortname)

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