import requests
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
from algo import return_summary


##server for flask app

app = Flask(__name__)

CORS(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dash')
def get_dash():
    return render_template('dash.html')

@app.route('/summ')
def get_summ():
    return render_template('summ.html')


@app.route('/ocr')
def get_ocr():
    return render_template('ocr.html')

@app.route('/results',methods=["GET","POST"])
def process_text():
    ##get the request from the sendData function
    ##put it throught the alorithm and return the formatted text
    
    data = request.get_json() 
    
    text=data['text']
    summary=return_summary(text)
    return [summary]


if( __name__ =='__main__'):
    app.run(debug=True)