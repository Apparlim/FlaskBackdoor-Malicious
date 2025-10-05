import os
from flask import Flask, request, redirect, flash, send_from_directory

FILES_PATH = '/usr/src/app/files'
app = Flask(__name__)
app.config['FILES_PATH'] = FILES_PATH

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['FILES_PATH'], filename)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file or not file.filename:
            flash('No file selected')
            return redirect(request.url)
        name = file.filename
        file.save(os.path.join(app.config['FILES_PATH'], name))
        return 'File uploaded successfully!'
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run()
