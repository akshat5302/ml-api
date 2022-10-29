from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from prophet.serialize import model_to_json, model_from_json

app=FastAPI()

class InputItem(BaseModel):
    
     year: int
     month: int 
    
with open('serialized_model.json', 'r') as fin:
    m = model_from_json(fin.read())  # Load model
    
@app.post('/')
async def scoring_endpoint(item:InputItem):
    df = pd.read_csv('fcast.csv')
    predictions=m.predict(df)
    ans=predictions.iloc[-1]['yhat']
    return {"predictions":int(ans)}