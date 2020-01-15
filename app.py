import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import mainFile

UPLOAD_FOLDER = "xmlCollection"
ALLOWED_EXTENSIONS = {'xml'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.close()
            return render_template('index.html', message="uploaded with success")
        return render_template('index.html', message="not uploaded")

    return render_template('index.html', message="upload")


@app.route("/request", methods=["POST", "GET"])
def search():
    content = ''
    if request.method == "POST":
        content = mainFile.a('xmlCollection', request.form['point'])
    return render_template('search.html', content=content)


if __name__ == "__main__":
    app.run()
