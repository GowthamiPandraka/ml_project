from flask import Flask,render_template,request
import pandas as pd
import pickle
import os
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/'
regressor=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/display',methods=['GET','POST'])
def uploader():
    if request.method == 'POST':
        SPX=float(request.form['SPX'])
        USO=float(request.form['USO'])
        SLV=float(request.form['SLV'])
        EUR_USD=float(request.form['EUR_USD'])
        input_data=(SPX,USO,SLV,EUR_USD)
        input_data_as_numpy_array=np.asarray(input_data)
        input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
        prediction=regressor.predict(input_data_reshaped)[0]
        prediction="{:.2f}".format(prediction)
        
        return render_template('display.html',result=prediction)

if __name__=='__main__':
    app.run(debug=True)
