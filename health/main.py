import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

import numpy as np

df =pd.read_csv("health_lifestyle_dataset.csv")
df = df.drop("gender" , axis = 1)
X = df.drop("disease_risk", axis = 1)
y = df["disease_risk"]


X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.3, random_state = 50)
scale = StandardScaler()
X_train_scale = scale.fit_transform(X_train)
X_test_scale = scale.fit_transform(X_test)


model = LogisticRegression(class_weight='balanced' ,solver = "saga" , max_iter = 10000)
model.fit(X_train_scale,y_train)

y_pred = model.predict(X_test_scale)

acc = accuracy_score(y_test,y_pred)
print("Accuracy:" ,acc)
cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix")
print(cm)