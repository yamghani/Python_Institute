from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_wine

from numpy import loadtxt
import csv

dataset = loadtxt('C:/Crescendo/Kenny.j/new_data_2.csv', delimiter=",")

X = dataset[:, 2:]
Y = dataset[:, 1]


seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
# fit model no training data
model = XGBClassifier()
model.fit(X_train, y_train)
# make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))


training_data_list = []
with open('C:/Crescendo/Kenny.j/new_data.csv', 'r') as file:
    csv_file = csv.DictReader(file)

    for row in csv_file:
        training_data_list.append(dict(row))
        # print(row['down'])
        # print(dict(row))

