import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder , StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

# In Python, the @dataclass decorator is used to simplify the creation of classes that are mainly used to store data. 
# When you define a class as a dataclass, Python automatically generates special methods for it, like __init__(), __repr__(), __eq__(), and __hash__() (if applicable), which reduces boilerplate code
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_columns=['reading_score', 'writing_score']
            categorical_columns=[
                'gender',
                'race_ethnicity', 
                'parental_level_of_education', 
                'lunch',       
                'test_preparation_course'
            ]

            
        except:
            pass