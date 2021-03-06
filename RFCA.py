# -*- coding: utf-8 -*-
"""RFC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NxuFIh_moLwWPQWfXzSEJgcXr7bGdC_C
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random as rd

m_map={
    'S':0,
    'C':1,
    'Q':2,
    ' ':4 
}

dataset = pd.read_csv('train.csv')
dataset=dataset.drop(columns=['Cabin','PassengerId','Name','Ticket'])
dataset['Survivors']=dataset['Survived']
dataset=dataset.drop(columns=['Survived'])
dataset['Age']=dataset['Age'].fillna(rd.randint(20,80))
dataset['Embarked']=dataset['Embarked'].map(m_map)
dataset=dataset.dropna(how='any')

X_train=dataset.iloc[:,:-1].values
y_train=dataset.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
X_train[:,1]=le.fit_transform(X_train[:,1])

X_train

df=pd.read_csv('test.csv',nrows=150)
a=df['PassengerId']
df=df.drop(columns=['Cabin','PassengerId','Name','Ticket'])
df['Age']=df['Age'].fillna(rd.randint(20,80))
df=df.dropna(how='any')
df['Embarked']=df['Embarked'].map(m_map)

X_test=df.iloc[:,:].values

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
X_test[:,1]=le.fit_transform(X_test[:,1])

X_test

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 250, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

ds=pd.read_csv('pred1.csv',nrows=150)
ds=ds.drop(columns=['PassengerId'])
ds=ds.dropna(how='any')

y_test=ds.iloc[:,:].values

y_pred = classifier.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(accuracy_score(y_test, y_pred)*100)