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
        choise = request.form['exercise']
        if choise == "a":
            tag = request.form['tag']
            content = mainFile.a('xmlCollection', tag)
        if choise == "b":
            tag = request.form['tag']
            tags = tag.split()
            if len(tags) != 2:
                content = ["wrong input try 'tag keyword' with space"]
            else:
                content = mainFile.b('xmlCollection', tags[0], tags[1])
        if choise == "c":
            count = int(request.form['tag'])
            print(count)
            content = mainFile.c('xmlCollection', count)
        if choise == "d":
            depth = int(request.form['tag'])
            print(depth)
            content = mainFile.d('xmlCollection', depth)

    return render_template('search.html', content=content)


@app.route("/read/<string:file_name>")
def read_file(file_name):
    content = open("xmlCollection/" + file_name).read()
    print(content)
    return "<pre><xmp>" + content + "<xmp></pre>"


if __name__ == "__main__":
    app.run(debug=True)
