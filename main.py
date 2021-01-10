import pickle
import sklearn
from module.predict import test
import cv2
import os
import glob
from dominate import document
from dominate.tags import *
from werkzeug.utils import secure_filename
from flask import Flask, render_template,request,redirect, url_for, send_from_directory
app =Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file',
                                filename=filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	PATH_TO_TEST_IMAGES_DIR = app.config['UPLOAD_FOLDER']
	TEST_IMAGE_PATHS = [os.path.join(PATH_TO_TEST_IMAGES_DIR,filename.format(i)) for i in range(1, 2)]
	for image_path in TEST_IMAGE_PATHS:
		out = test(image_path)
		photos = glob.glob(os.path.join("/uploads/",filename))
		path_out="{{url_for('static', filename='"+str(filename)+"')}}"
		print(path_out)
		text = "This is our result: "+str(out)
	with document(title='ket qua') as doc:
		h1(text,align="middle")
		div(img(src=path_out), _class='photo',align="middle")
		# div(p(output),align="middle")
	with open('./templates/gallery.html', 'w') as f:
		    f.write(doc.render())
	return render_template('./gallery.html')
if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=5000)