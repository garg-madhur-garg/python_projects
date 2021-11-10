import requests
import pickle
# Download iris data from given url
r = requests.get("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

with open("iris.txt", "w")as f:
    c = f.write(r.text)
# convert file content into list
with open("iris.txt")as f:
    c = list(f.readlines())
# pickling
with open("iris.txt", "wb")as fileobj:
    pickle.dump(c, fileobj)

# depickling
with open("iris.txt", "rb")as fileobj:
    loadvalue = pickle.load(fileobj)
    print(loadvalue)
