import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error
import pickle

"""
This file is for creating the random forest model. 
Testing which model and which split size was determined
in the regression.ipynb notebook. 
"""

df = pd.read_csv('./data/cleaned_universities.csv')

df['school_type'] = df['school_type'].astype("category")
# converts the school_type column to a cateogry dtype

df['school_type_codes'] = df['school_type'].cat.codes
# makes numerical codes for each school type
# 0 = private
# 1 = public

X = df.drop(columns=['school_type', 'Graduation rate'])
# independant features
y = df['Graduation rate']
# dependant feature

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
# split the data into testing and training datasets. 

rf = RandomForestRegressor()
rf.fit(X_train, y_train)

# with open('model.pkl', 'wb') as file:
#     pickle.dump(rf, file)

# makes the pickle file for the model to load into. 
# this is commented out so it doesn't get replaced every time