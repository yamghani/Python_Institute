import copy
import csv

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures

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


# with open('C:/Personal/Python_Institute/training_data.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)

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

y_temp[y_temp == 'GREEN'] = 1
y_temp[y_temp == 'YELLOW'] = 2
y_temp[y_temp == 'RED'] = 3

x_train, x_test, y_train, y_test = train_test_split(X, y_temp, test_size=0.3, random_state=140)

ml = LinearRegression()
ml.fit(x_train, y_train)

y_pred = ml.predict(x_test)
r2_score(y_test, y_pred)

# ---------------------------------------
ml_2 = PolynomialFeatures(degree=3, include_bias=False)
poly_features = ml_2.fit_transform(x_train)
poly_reg_model = LinearRegression()
poly_reg_model.fit(poly_features, y_train)

y_pred = ml.predict(x_test)
r2_score(y_test, y_pred)

plt.figure(figsize=(15, 10))
plt.scatter(y_test, y_pred)
plt.xlabel('Actual')
plt.ylabel('Prediction')
plt.title('Actual vs. Predicted')


df = pd.DataFrame(X, columns=['throughput', 'cpu', 'ram', 'cc'])
corrMatrix = df.corr()
seabornInstance.heatmap(corrMatrix, annot=True)
plt.show()
