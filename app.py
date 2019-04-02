import os
from flask import Flask , render_template, url_for,request, redirect, flash, send_from_directory
app = Flask(__name__)





@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')



@app.route("/about")
def about():
    return render_template('about.html')





UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'webp', 'svg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER





def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route("/upload", methods=['GET', 'POST'])
def upload_xray():
    if request.method == 'POST' :
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            #uploadAddress = filename
            print('inside upload x-ray : ', filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return uploaded(filename)
    return render_template('upload.html')



def uploaded(filename):
    print('inside uploaded : ', filename)
    return render_template('uploaded.html', filename=filename )





@app.route("/generate")
def generate():
    return render_template('generate.html')

#set FLASK_APP=app.py
#set FLASK_DEBUG=1