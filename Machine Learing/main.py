import matplotlib.pyplot as mpl
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

# (['data', 'target', 'DESCR', 'feature_names', 'data_filename', 'target_filename'])
diabetes = datasets.load_diabetes()

diabetes_x = diabetes.data
# Features

diabetes_train_x = diabetes_x[:-30]
diabetes_test_x = diabetes_x[-30:]

# Labels
diabetes_train_y = diabetes.target[:-30]
diabetes_test_y = diabetes.target[-30:]

# Model
model = linear_model.LinearRegression()
model.fit(diabetes_train_x, diabetes_train_y)

# Predict
diabetes_predict_y = model.predict(diabetes_test_x)

# Check error
print(f"Your mean square error is {mean_squared_error(diabetes_test_y, diabetes_predict_y)}")

print(f"Weight: {model.coef_}")
print(f"Intercept: {model.intercept_}")

# Plotting
# mpl.scatter(diabetes_test_x, diabetes_test_y)
# mpl.plot(diabetes_test_x, diabetes_predict_y)
# mpl.show()