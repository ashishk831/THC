"""
This is a boilerplate pipeline 'split_data'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import split_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
            node(func=split_data,
                  inputs="processed_data", 
                  outputs=["X_train", "X_test", "y_train", "y_test"])
        ])
