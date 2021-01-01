import os
import pandas as pd 
import numpy as np 
import flask
import pickle
from flask import Flask, render_template, request
app=Flask(__name__)
@app.route("/")
def index():
 return flask.render_template("home.html")



def ValuePredictor(speed):
 to_predict = speed
 loaded_model = pickle.load(open('model.pkl','rb'))   #Load in the model
 result = loaded_model.predict([[to_predict]])  #use the predict function in the model and pass in speed value
 return result[0]


@app.route("/predict",methods = ["POST"])
def result():
 if request.method == "POST":
   speed = first_name = request.form.get("speed")  # Get the speed value entered
   result = ValuePredictor(speed)  # Pass the speed value into the model and return the result
   prediction = str(result)
   return render_template("PowerResult.html",prediction=prediction)  #Render result on a new page
if __name__ == '__main__':
  app.run(debug=True)