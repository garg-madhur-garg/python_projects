'''Train a logistic regression to predict whether a flower is iris-verginica or not'''

from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np
iris = datasets.load_iris()

feature = iris.data[:, 3:]
label = (iris.target == 2).astype(np.int)

# Train logistive regression classifier

clf = LogisticRegression()
clf.fit(feature, label)

example = clf.predict([[2.9]])
print(example)

# Using matplotlib to plot the visualization

x_new = np.linspace(0, 3, 1000).reshape(-1, 1)
y_prob = clf.predict_proba(x_new)
plt.plot(x_new, y_prob[:, 1], "g-", label="Verginica")
plt.show()