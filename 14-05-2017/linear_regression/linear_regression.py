import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

#read data
dataframe = pd.read_fwf('data_linear_regression.txt')
x_values = dataframe[['intrest']]
y_values = dataframe[['price']]

#train model on data
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)
x = 11
y = body_reg.predict(x)

#visualize results
plt.scatter(x_values, y_values)
plt.scatter(x,y,color='red')
plt.plot(x_values, body_reg.predict(x_values) ,color='green')
plt.show()
