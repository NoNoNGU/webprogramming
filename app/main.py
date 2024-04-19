from typing import Union

from fastapi import FastAPI

import requests

app = FastAPI()

@app.get("/")
def root():
    URL = "https://bigdata.kepco.co.kr/openapi/v1/powerUsage/industryType.do?year=2020&month=11&metroCd=11&cityCd=110&apiKey=76abU171NsT6039587k9RS061dnAIjP871dmDw1h&returnType=json"

    contents = requests.get(URL).text

    return { 'message': contents}

@app.get("\home")
def home():
    return {"message": "Home!"}