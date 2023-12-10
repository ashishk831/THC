"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 0.18.14
"""
from sklearn.ensemble import RandomForestRegressor

def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators = 10, random_state = 0)
    model.fit(X_train, y_train)
    return model

