# Import required modules
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# Loading datasets
iris = datasets.load_iris()

# Printing features and description
features = iris.data
label = iris.target
# print(iris.DESCR)

# Training the Classifier
clf = KNeighborsClassifier()
clf.fit(features, label)

# Do Prediction
pred = clf.predict([[100, 500, 600, 400]])
print(pred)