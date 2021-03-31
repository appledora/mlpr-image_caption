from flask import Flask, render_template, url_for, request, redirect
from generator import *
import warnings
warnings.filterwarnings("ignore")



app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/', methods = ['POST'])
def upload_file():
	if request.method == 'POST':
		img = request.files['image']
		img.save("images/"+img.filename)


		caption = caption_this_image("images/"+img.filename)


		result_dic = {
			'image' : "/home/mr/Documents/FluskStuff/ML-Models-Flask/ImageCaptionGenerator/images/" + img.filename,
			'description' : caption
		}
		print(result_dic)
	return render_template('index.html', results = result_dic)



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5555,debug = True)