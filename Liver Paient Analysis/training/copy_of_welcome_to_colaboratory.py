# -*- coding: utf-8 -*-
"""Copy of Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IAeWlYqZunoxLvsZmGSq67iblRd9pBlc
"""



import pandas as pd

import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt

from matplotlib import rcParams

from scipy import stats

data=pd.read_csv(r'/content/sample_data/indian_liver_patient.csv')
data.head()

data.info()

data.isnull().any()

data.isnull().sum()

#data['Albumin_and_Globulin_Ratio']=data.fillna(data['Albumin_and_Globulin_Ratio'].mode()[0])

data.isnull().sum()

from sklearn.preprocessing import LabelEncoder
lc=LabelEncoder()
data['Gender']=lc.fit_transform(data['Gender'])

data.describe()

sns.distplot(data['Age'])
plt.title('Age Distribution Graph')
plt.show()

#sns.countplot(data['outcome'],hue=data['Gender'])

plt.figure(figsize=(10,7))

#sns.heatmap(df.corr(),annot=True)

from sklearn.preprocessing import scale
#X_scaled=pd.DataFrame(scale(X),columns=X.columns)
#X_scaled.head()

X=data.iloc[:,:-1]
#y=data.outcome

from sklearn.model_selection import train_test_split

#X_train,X_test,y_train,y_test=train_test_split(X_scaled,y,test_size=0.2,random_state=42)

pip install imblearn

from imblearn.over_sampling import SMOTE
smote=SMOTE()

#y_train.value_counts()

#X_train_smote,y_train_smote=smote.fit_resample(X_train,y_train)

#y_train_smote.value_counts()

from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
model1=RandomForestClassifier()
#model1.fit(X_train_smote,y_train_smote)
#y_predict=model1.predict(X_test)
#rfc1=accuracy_score(y_test,y_predict)
#rfc1
#pd.crosstab(y_test,y_predict)
#print(classification_report(y_test,y_predict))

from sklearn.tree import DecisionTreeClassifier
model4=DecisionTreeClassifier()

model4.fit #(X_train_smote,y_train_smote)
y_predict=model4.predict #(X_test)
dtc1=accuracy_score #(y_test,y_predict)
dtc1
#pd.crosstab(y_test,y_predict)
#print(classification_report(y_test,y_predict))

from aklearn.neighbors import kneighborsclassofier
model2=kneighborsclassifier()
model2.fit(X_train_smote, y_train_smote)
y_predict = model2.predict(x_test)
knn1=(accuracy_score(y_test, y_predict))
knn1
pd.crosstab(y_test,y_predict)
print (classification_report(y_test,y_predict))

from sklearn.linear_model import logisticregression
model5=logisticregression()
model5.fit(X_train_smote, y_train_smote)
y_predict=model5.predict(X_test)
logi1=accuracy_score(y_test,y_predict)
logi1
pd.crosstab(y_test,y_predict)
print(classification_report(y_test,y_predict))

impoer tensorflow.keras
from tensorflow.keras.models import sequential
from tensorflow.keras.layers import Dense

# Initialising the ANN
classifier = sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units=100, activation='renu', input_dim=10))

# Adding the second hidden layer 
classifier.add(dense(units=50,activation='renu'))

# adding the output layer 
classifier.add(dense(units=1,activation='sigmoid'))

# compiling the ANN
classifier.compile(optimizer='adam',loss='binary_crossentropy', metrics=['accuracy]')

# fitting the ANN to the training set 
model_history = classifier.fit(X_train, y_train, batch_size=100, validation_spilt=0.2, epochs=100)

#age gender total bilrubin direct bilrubin"alkaline_phosphotase alantin_aminotransferase asparate_aminotrans.
model4.predict([[50,1,1.2,0.8,150,70,80,7.2,3.4,0.8]])

#age gender total bilrubin direct bilrubin"alkaline_phosphotase alanin_aminotransferase asparate_aminotrans 
model1.predict([[50,1,1.2,0.8,150,70,80,7.2,3.4,0.8]])

classifier.save("liver.h5")

y_pred = classifier.predict(X_test)

y_pred

y_pred = (y_pred > 0.5)
y_pred

predict_exit(sample value):

convert list to numpy array 
sample_value = np.array(samply_value)

reshape because sample_value contains only 1 record
sample_value = sample_value.reshape(1,-1)

feature scaling
sample_value = scale(sample_value)

return classifier.predict(sample_value)

#age gender total bilrubin direct bilrubin alkaline_phosphotase 
sample_value = [[50,1,1.2,0.8,150,70,80,7.2,3.4,0.8]]
if predict_exist(sample_value)>0.5:
    print('prediction:liver patient')
else:
    print('prediction:healthy')

acc_smote= [['KNN classifier' , knn1],   ['randomforestclassifier' , rfc1],
            ['dicisiontreeclassifier' , dtc1],['logisticregression' , logi1]]
liverpatient_pred=pd.dataframe(acc_smote, columns = ['classification models','accuracy_score'])
liverpatient_pred

plt.figure(figsize=(7,5))
plt.xticks(rotation=90)
plt.title('classification models & accuracy scores after SMOTE',fontsize=18)
sns.barplot(X="classification models", y="accuracy_score", data=liverpatient_pred,palette ="set2")

from sklearn.ensemble import extratreesclassifier
model-extratreesclassifier()
model.fit(x,y)

model.feature_importances_

dd=pd.dataframe(model.feature_importance_,index=X.columns).sort_values(0,ascending=false)
dd

dd.plot(kind='birth', figsize=(7,6))
plt.title("FEATURE IMPORTANCE", fontsize=14)

import joblib
joblib.dump(model1, 'ETC.pkl')

from flask import flask, render_template, request
import pickle

app=flask(_name_)

@app.route('\')
def home():
    return render_template('home.html')
@app.route('\predict')
def index() :
    return render_template("index.html")

@app.route('\data_predict', methods=['post'])
def predict():
    age = request.form['Age']
    gender = request.form['Gender']
    tb = request.form['tb']
    db = request.form['db']
    ap = request.form['ap']
    aa1 = request.form['aa1']
    aa2 = request.form['aa2']
    tp = request.form['tp']
    a = request.form['a']
    agr = request.form['agr']

    data = [[float(age), float(gender), float(tb), float(db), float(ap), float(aa1), float(aa2), float(tp),
             
    #model = pickle.load(open('liver_analysis.pk1', 'rb'))

    #prediction= model.predict(data)[0]
    #if (prediction == 1):
    #return render_template('nochance.html', prediction='you have a liver desease problem,')
#if _name_ =='_main_';
#app.run()

#if _name_=='_main_';
#app.run()