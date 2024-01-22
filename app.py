from flask import Flask, render_template, request
import numpy as np
import os
from model import predict, base
#import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)


UPLOAD_FOLDER = '/Users/adityavs14/Documents/Internship/Pianalytix/Month_2/EEGSeizure/app/static'
ALLOWED_EXTENSIONS = set(['png','jpg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

df = pd.read_csv(f'{base}/Epileptic Seizure Recognition.csv')
df = df.drop(columns = df.columns[0]) 



@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        plt.switch_backend('Agg')
        file1 = int(request.form['file1'])
        plt.plot(df.iloc[file1, :177].values)
        plt.savefig(f'{UPLOAD_FOLDER}/signal.png')
        s = predict(file1)
    return render_template('index.html', result=s) 





if __name__ == "__main__":
    app.run(debug=True)