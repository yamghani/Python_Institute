import copy
import csv

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import uniform, randint

from sklearn.datasets import load_breast_cancer, load_diabetes, load_wine
from sklearn.metrics import auc, accuracy_score, confusion_matrix, mean_squared_error
from sklearn.model_selection import cross_val_score, GridSearchCV, KFold, RandomizedSearchCV, train_test_split

import xgboost as xgb


def display_scores(scores):
    print("Scores: {0}\nMean: {1:.3f}\nStd: {2:.3f}".format(scores, np.mean(scores), np.std(scores)))


def report_best_scores(results, n_top=3):
    for i in range(1, n_top + 1):
        candidates = np.flatnonzero(results['rank_test_score'] == i)
        for candidate in candidates:
            print("Model with rank: {0}".format(i))
            print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
                  results['mean_test_score'][candidate],
                  results['std_test_score'][candidate]))
            print("Parameters: {0}".format(results['params'][candidate]))
            print("")


throughput = 1
cpu = 1
ram = 1
cc = 1


def get_status(throughput, cpu, ram, cc):
    throughput_coeff = 0.00566473
    cpu_coeff = 0.00491729
    ram_coeff = 0.00491567
    cc_coeff = 0.00792113
    intercept = 1.5472540002295014
    ml_output = intercept + throughput_coeff*throughput + cpu_coeff*cpu + ram_coeff*ram + cc_coeff*cc
    result = np.floor(ml_output)
    if result < 2:
        return 'GREEN'
    elif result < 3:
        return 'YELLOW'

    return 'RED'


red_counter = 0
yellow_counter = 0
green_counter = 0
with open('C:/Personal/Python_Institute/training_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['status'] == 'GREEN':
            green_counter += 1
        elif row['status'] == 'YELLOW':
            yellow_counter += 1
        elif row['status'] == 'RED':
            red_counter += 1
        # print(row['throughput'], ':', row['cpu'], ':', row['ram'], ':', row['cc'], ':', row['status'])

# 9019271
# 8975104
# 82005625
print(green_counter)
print(yellow_counter)
print(red_counter)

dataset = pd.read_csv('C:/Personal/Python_Institute/training_data.csv')

print(dataset.shape)
print(dataset.describe())

#         Unnamed: 0    throughput           cpu           ram            cc
# count  1.000000e+08  1.000000e+08  1.000000e+08  1.000000e+08  1.000000e+08
# mean   5.000000e+07  5.050000e+01  5.050000e+01  5.050000e+01  5.050000e+01
# std    2.886751e+07  2.886607e+01  2.886607e+01  2.886607e+01  2.886607e+01
# min    0.000000e+00  1.000000e+00  1.000000e+00  1.000000e+00  1.000000e+00
# 25%    2.500000e+07  2.575000e+01  2.575000e+01  2.575000e+01  2.575000e+01
# 50%    5.000000e+07  5.050000e+01  5.050000e+01  5.050000e+01  5.050000e+01
# 75%    7.500000e+07  7.525000e+01  7.525000e+01  7.525000e+01  7.525000e+01
# max    1.000000e+08  1.000000e+02  1.000000e+02  1.000000e+02  1.000000e+02

print(dataset.head())

dataset_1 = dataset.drop(['Unnamed: 0'], axis=1).values
X = dataset_1[:, 0:4]
y = dataset_1[:, 4]
# X = dataset_1.drop(['status'], axis=1).values

y_temp = copy.deepcopy(y)

y_temp[y_temp == 'GREEN'] = 0
y_temp[y_temp == 'YELLOW'] = 1
y_temp[y_temp == 'RED'] = 2

xgb_model = xgb.XGBClassifier(objective="multi:softprob", random_state=42)
xgb_model.fit(X, y_temp)

y_pred = xgb_model.predict(X)

print(confusion_matrix(y, y_pred))
