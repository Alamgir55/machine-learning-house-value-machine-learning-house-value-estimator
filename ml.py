from sklearn import tree
from sklearn.datasets import load_iris
iris = load_iris()
print(list(iris.target_names))

classifier = tree.DecisionTreeClassifier()
# print(iris.data)
# print(iris.target)
classifier = classifier.fit(iris.data, iris.target)
print(classifier.predict([[5.1, 3.5, 1.4, 0.2]]))
