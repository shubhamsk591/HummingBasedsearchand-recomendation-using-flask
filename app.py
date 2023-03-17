#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
import os
import glob
import librosa
import Processing.fingerprint as fp
import Processing.recognise as final
import Processing.featureExtract as fe
import Processing.recommend as final1
app = Flask(__name__)

list=[]
@app.route("/", methods=['POST', 'GET'])

def index():
    if request.method == "POST":
        files = glob.glob('test_data/*')
        for f in files:
            os.remove(f)
        f = request.files['audio_data']
        with open('test_data/audio.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')
        return render_template('index.html', request="POST")
    else:
        return render_template("index.html")

@app.route('/recognise', methods = ['GET', 'POST'])
def recognise():
    
    fp1=fp.fingerprint("test_data/audio.wav")
    print("Fingerprint Completed")
    list=final.result(fp1)
    return render_template('recognise.html', **locals()) 

@app.route('/redirect')
@app.route('/recommend', methods = ['GET', 'POST'])
def recommend():
    
    fp1=fe.extract_features("test_data/audio.wav")
    print("Feature Extraction Completed")
    list=final1.result(fp1)
    return render_template('recommendation.html', **locals()) 
if __name__ == "__main__":
    app.run(debug=True)