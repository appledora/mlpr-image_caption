from flask import Flask, render_template, url_for, request, redirect
from generator import *
import os 
import warnings
warnings.filterwarnings("ignore")

dir_path = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__ , static_url_path='/static')

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def upload_file():
	if request.method == 'POST':
		img = request.files['image']
		img.save("static/"+img.filename)

		caption = caption_this_image("static/"+img.filename)

		result_dic = {
			'image' : dir_path +"/static/" + img.filename,
			'description' : caption,
			'filename' : img.filename,
		}
		print(result_dic)
	return render_template('index.html', results = result_dic)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5555,debug = True)