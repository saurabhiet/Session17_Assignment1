import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import sklearn
from pandas import Series, DataFrame
from pylab import rcParams
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
url="https://raw.githubusercontent.com/BigDataGal/Python-for-Data-Science/master/titanic-train.csv"
titanic = pd.read_csv(url)
titanic.columns = ['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']
titanic = titanic.drop(['Cabin'], axis = 1)
titanic = titanic.drop(['Ticket'], axis = 1)
titanic["Age"] = titanic["Age"].fillna(-0.5)
bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
titanic = titanic.drop(['Name'], axis = 1)
titanic = titanic.drop(['Embarked'], axis = 1)
sex_mapping = {"male": 0, "female": 1}
titanic['Sex'] = titanic['Sex'].map(sex_mapping)
for x in range(len(titanic["Fare"])):
    if pd.isnull(titanic["Fare"][x]):
        pclass = titanic["Pclass"][x] #Pclass = 3
        titanic["Fare"][x] = round(titanic[titanic["Pclass"] == pclass]["Fare"].mean(), 4)

print(titanic.head())

predictors = titanic.drop(['Survived', 'PassengerId'], axis=1)
target = titanic["Survived"]
x_train, x_val, y_train, y_val = train_test_split(predictors, target, test_size = 0.22, random_state = 0)

logreg = LogisticRegression()
logreg.fit(x_train, y_train)
y_pred = logreg.predict(x_val)
acc_logreg = round(accuracy_score(y_pred, y_val) * 100, 2)
print()
print (acc_logreg)
