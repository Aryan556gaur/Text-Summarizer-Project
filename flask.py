import sys
import os
from flask import Flask,request
from textSummarizer.pipeline.prediction import PredictionPipeline


text:str = "What is Text Summarization?"

app = Flask(__name__)
application=app

@app.get("/")
def index():
    return ("Welcome")



@app.get("/train")
def training():
    try:
        os.system("python main.py")
        return ("Training successful !!")

    except Exception as e:
        return (f"Error Occurred! {e}")
    



@app.get("/predict")
def predict_route():
    try:

        obj = PredictionPipeline()
        text = obj.predict('Great",Olivia and Olivier are voting for liberals in this election')
        return text
    except Exception as e:
        raise e
    

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)
