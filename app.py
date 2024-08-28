from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
app=Flask(__name__)
diabetes_predict=pickle.load(open('diabetes.pkl', 'rb'))
heart_predict=pickle.load(open('heart.pkl', 'rb'))
@app.route('/') 
def home():
    return render_template("home.html")
@app.route('/diabetes') 
def diabetes():
    return render_template("diabetes.html")
@app.route('/heartdisease/') 
def heartdisease():
    return render_template("heartdisease.html")
@app.route('/predictdiabetes/',methods=['POST']) 
def predictdiabetes(): 
    int_features=[x for x in request.form.values()]
    processed_feature_diabetes=[np.array(int_features,dtype=float)]
    prediction=diabetes_predict.predict(processed_feature_diabetes)
    if prediction[0]==1:
        display_text="The patient has high chances of Diabetes"
    else:
        display_text="The patient dosen't show possibility of Diabetes"
    return render_template('diabetes.html',output_text="Result: {}".format(display_text))
@app.route('/predictheartdisease/',methods=['POST']) 
def predictheartdisease():  
    int_features=[x for x in request.form.values()]
    processed_feature_heart=[np.array(int_features,dtype=float)]
    prediction=heart_predict.predict(processed_feature_heart)
    if prediction[0]==1: 
        display_text="The patient has high chances of Heart Stroke"
    else:
        display_text="The patient dosen't show possibility of Heart Stroke"
    return render_template('heartdisease.html',output_text="Result: {}".format(display_text))
if __name__=="__main__":
    app.run(debug=True)