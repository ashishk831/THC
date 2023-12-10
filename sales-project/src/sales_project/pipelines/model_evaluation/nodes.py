"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.18.14
"""
import numpy as np
import logging
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, max_error

def evaluate_model(model, X_test, y_test):
    """Calculates and logs the coefficient of determination.

    Args:
        model: Trained model.
        X_test: Testing data of independent features.
        y_test: Testing data for price.
    """
    y_pred = model.predict(X_test)
    mae=mean_absolute_error(y_test, y_pred)
    mse=mean_squared_error(y_test, y_pred)
    rmse=np.sqrt(mse)
    r2score=r2_score(y_test, y_pred)
    me = max_error(y_test, y_pred)
    print("MAE Of Model is: ",mae)
    print("MSE Of Model is: ",mse)
    print("RMSE Of Model is: ",rmse)
    print("R2_Score Of Model is: ",r2score)
    logger = logging.getLogger(__name__)
    logger.info("Model has a coefficient R^2 of %.3f on test data.", r2score)
    return {"r2_score": r2score, "mae": mae, "max_error": me}
    #return mae,mse,rmse,r2_score

