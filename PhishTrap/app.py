from flask import Flask, render_template, request
# Extract features from given url
from parallel_tqdm_v6 import extract_features
# To check if a url is active by inspecting the HTTP response code.
from is_active import check_active_url
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
import os
import math

app = Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))
# Load sklearn classifiers
import tensorflow as tf
models = []  
models.append(('KNN',joblib.load("{}/models/model_knn_opt.sav".format(dir_path)) )) 
models.append(('MLP',joblib.load("{}/models/model_mlp_opt.sav".format(dir_path)) )) 
models.append(('Random Forest',joblib.load("{}/models/model_rf_opt.sav".format(dir_path)) )) 
models.append(('Gradient Boosting', joblib.load("{}/models/model_gb_opt2.sav".format(dir_path)) )) 
# Load CNN model
models.append(('CNN',tf.keras.models.load_model("{}/models/model_cnn_opt.h5".format(dir_path)))) 

# Transformer to scale the data
sc = StandardScaler()
# Read the train data and transform them
df_train = pd.read_csv("./train3_int.csv")
X_train = sc.fit_transform(df_train.iloc[:,:-1])

constant_Phishing = math.log(0.12)
constant_Legit = math.log(0.88)
counter = 0
counter_legit = 0
counter_phishing =0

@app.route('/', methods=['GET','POST'])
def parse_urls():
    global counter
    global counter_legit
    global counter_phishing
    if request.method == 'GET' :
        return render_template( 'index.html',
                                counter= counter,
                                counter_legit = round(100 * counter_legit/ counter,2) if counter !=0 else 0,
                                counter_phish = round(100 * counter_phishing/ counter,2) if counter !=0 else 0,
                                load_form= True)
    elif request.method == 'POST':
        # Read post input by user
        url = request.form['url']
        # Check if the url is active
        _ , is_active = check_active_url(url,timeout = 1)   
        if is_active :
            # Increase counter of recieved requests
            counter += 1
            # Get the features of the url
            parsed_url = extract_features(url)
            # 1D to 2D
            df = np.array(parsed_url).reshape(1, -1)
            #Scale it based on the X_train
            df = sc.transform(df) 
            # List of answers
            ans = []
            # U is the voting scheme.
            u = {'PH':constant_Phishing, 'LEG':constant_Legit}            
            for model_name , model  in models :
                
                if not model_name.startswith('CNN') :
                    # sklearn Classifiers
                    pred = model.predict_proba(df)[0]
                else :
                    # This is a CNN model -> Data needs reshaping.
                    df = np.array([x / 12790.0 for x in parsed_url]).reshape(-1,63,1)
                    preds = model.predict(df)[0][0]
                    pred = [1 - preds, preds]
                # If pred = 0.0 then we have to change it because math.log(0.0) -> -∞
                if pred[0] == 1.0 :
                    pred[0] = 0.999
                    pred[1] = 0.001
                elif pred[1] == 1.0:
                    pred[0] = 0.001
                    pred[1] = 0.999
                
                if pred[0] > pred[1]:
                    u['LEG'] += math.log(pred[0]/(1-pred[0]))
                else :
                    u['PH']  += math.log(pred[1]/(1-pred[1]))
                    
                prob = pred[0] if pred[0] > pred[1] else pred[1]    #Highest probability --> Class predicted
                phishing = 'Legitimate' if pred[0] > pred[1] else 'Phishing'
                ans.append( (model_name,phishing,str(round(100*prob,2))+' %') )

            # Voting scheme. Increase proper counter
            if u['PH'] < u['LEG'] :
                counter_legit +=1
                overall = ('Legitimate', '')
            else  :
                counter_phishing +=1
                overall = ('Phishing',   '')
                
            return render_template('index.html',
                                   answer = ans,
                                   error_message = None,
                                   url = url,
                                   overall = overall,
                                   disclaimer = True,
                                   counter= counter,
                                   counter_legit = round(100 * counter_legit/ counter,2) if counter !=0 else 0,
                                   counter_phish = round(100 * counter_phishing/ counter,2) if counter !=0 else 0,
                                   load_form= False)
        else :
            #Can't manage to connect, url doesn't seem active.
            return render_template('index.html',
                                   error_message='Did not manage to connect to url. Seems inactive. Try again!',
                                   answer = None,
                                   url = url,
                                   overall = None,
                                   disclaimer= False,
                                   counter= counter,
                                   counter_legit = round(100 * counter_legit/ counter,2) if counter !=0 else 0,
                                   counter_phish = round(100 * counter_phishing/ counter,2) if counter !=0 else 0,
                                   load_form= False)
    else :
        return render_template('index.html',load_form= True)
		
if __name__=="__main__":
    app.run(host="0.0.0.0", port="8080",debug=False)
        
        
