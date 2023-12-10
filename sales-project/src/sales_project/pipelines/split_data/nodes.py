"""
This is a boilerplate pipeline 'split_data'
generated using Kedro 0.18.14
"""

import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(processed_data: pd.DataFrame):
    X = processed_data.drop(["Approved_Conversion","xyz_campaign_id","fb_campaign_id"], axis=1)
    y = processed_data["Approved_Conversion"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
    return X_train, X_test, y_train, y_test