import uvicorn 
import pandas as pd
import numpy as np 
from  fastapi import FastAPI
import joblib


from inputbmi import bmiinput
model=joblib.load("bmimodel.joblib")
app=FastAPI()
@app.post("/predictbmi")
def predictbmi(data:bmiinput):
    data=data.model_dump()
    age=data["age"]
    height=data["height"]
    weight=data["weight"]

    host_data=[age,height,weight]
    pred_result=model.predict([host_data])
    
    output=float(pred_result[0])
    return{"prediction":output}


if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=4000)
