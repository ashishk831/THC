"""
This is a boilerplate pipeline 'data_preprocessing'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import preprocessing


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=preprocessing,
             inputs="sale_data",
             outputs="processed_data")
    ])

