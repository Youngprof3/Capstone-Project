import uvicorn
from fastapi import FastAPI
from features import feature
import numpy as np
import pickle
import pandas as pd

app = FastAPI()
with open("clf.pkl","rb") as f:
    clf = pickle.load(f)

@app.get('/')
def index():
    return {'message': 'Hello World'}

@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome to Arinze Model Deployment Page': f'{name}'}

@app.post('/predict')
def Terrorist_Attack(data:feature):
    data = data.dict()
    Year = data['Year']
    Month = data['Month']            
    Day = data['Day']      
    Extended = data['Extended']    
    Suicide = data['Suicide']        
    Attack_Group = data['Attack_Group']   
    No_Of_Killed = data['No_Of_Killed']   
    No_Of_Wounded = data['No_Of_Wounded'] 
    Property = data['Property']   
    country = data['country']   
    region = data['region']   
    attacktype1 = data['attacktype1']   
    targtype1 = data['targtype1']  
    natlty1 = data['natlty1']   
    weaptype1 = data['weaptype1']      
    

    print(clf.predict([[Year, Month, Day, Extended, Suicide, Attack_Group,
       No_Of_Killed, No_Of_Wounded, Property, country, region,
       attacktype1, targtype1, natlty1, weaptype1]]))
    prediction = clf.predict([[Year, Month, Day, Extended, Suicide, Attack_Group,
       No_Of_Killed, No_Of_Wounded, Property, country, region,
       attacktype1, targtype1, natlty1, weaptype1]])
    if(prediction[0] == 1):
        prediction = 'Successful Terrorist Attack'
    else:
        prediction = 'Unsuccessful Terrorist Attack'
    return{'prediction': prediction}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
#uvicorn app:app --reload
