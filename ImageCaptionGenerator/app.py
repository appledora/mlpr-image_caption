from flask import Flask, render_template, flash, request, redirect
from generator import *
import os
import warnings
import pandas as pd
warnings.filterwarnings("ignore")

dir_path = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__, static_url_path='/static')
app.secret_key = os.urandom(8)


def write_to_CSV(df):
    if not os.path.isfile('CaptionDataset.csv'):
        df.to_csv('CaptionDataset.csv')
    else:  # else it exists so append without writing the header
        df.to_csv('CaptionDataset.csv', mode='a', header=False)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        img = request.files['image']
        img.save("static/"+img.filename)
        caption = caption_this_image("static/"+img.filename)
        result_dic = {
            'image': dir_path + "/static/" + img.filename,
            'description': caption,
            'filename': img.filename,
        }
    return render_template('index.html', results=result_dic)


@app.route('/getRate', methods=['POST'])
def save_data():
    opt = None
    capt = None
    try:
        opt = request.form['options']
        print("opt : ", capt)
    except:
        print("opt is null")

    try:
        capt = request.form['captionSuggestion']
        print("capt : ", capt)
    except:
        print("capt is null")
    name = request.form["fname"]
    res = request.form["fval"]
    df = pd.DataFrame.from_records([{
        "Filename": name,
        "Generated Caption": res,
        "User Rating": opt,
        "Suggested Caption": capt
    }])
    print("DF -> ", df)
    write_to_CSV(df)
    return redirect("/")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
