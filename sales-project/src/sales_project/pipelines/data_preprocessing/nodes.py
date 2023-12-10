"""
This is a boilerplate pipeline 'data_preprocessing'
generated using Kedro 0.18.14
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def preprocessing(data: pd.DataFrame):    
    data.gender = data.gender.apply(lambda x: 1 if x=="M" else 0)
    data['CTR'] = ((data['Clicks']/data['Impressions'])*100)
    data['CPC'] = data['Spent']/data['Clicks']
    data['CPC'] = data['CPC'].replace(np.nan,0)
    encoder=LabelEncoder()
    encoder.fit(data["age"])
    data["age"]=encoder.transform(data["age"])
    preprocessed_data = data.copy()
    return preprocessed_data

