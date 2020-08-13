# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 00:13:13 2020

@author: gupta
"""


import pandas as pd
df = pd.read_csv('train.csv')
df.isnull().sum()
df[df['Embarked'].isnull()]
import numpy as np
df['Cabin_null'] = np.where(df['Cabin'].isnull(),1,0)


df.groupby(['Survived'])['Cabin_null'].mean()
df = pd.read_csv('Train.csv',usecols = ['Age','Fare','Survived'])

df.head()
df.isnull().mean()
def impute_nan(df,variable,median):
    df[variable+'_median'] = df[variable].fillna(median)

median = df.Age.median()
median

impute_nan(df, 'Age', median)
