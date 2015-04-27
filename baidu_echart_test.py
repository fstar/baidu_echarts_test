from flask import Flask,request,redirect,url_for
from flask import render_template
from werkzeug import secure_filename
import os



app = Flask(__name__)
UPLOAD_FOLDER = '/static/Uploads'

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test',methods=['GET','POST'])
def test():
    dic = {}
    if request.method == "POST":
        f = request.files['file']
        if f.filename != None:
            fname = secure_filename(f.filename)
            f.save(os.path.join(os.getcwd(),UPLOAD_FOLDER,fname))
    return render_template("baidu_map_test.html")


if __name__ == '__main__':
    app.run(debug=True)
