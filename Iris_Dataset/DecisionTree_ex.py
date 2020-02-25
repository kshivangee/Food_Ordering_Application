import boto3
from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
import graphviz
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

#Creating a file to store the output to the S3 bucket
f = open("DecisionTree_output.txt","w+")

#Load the data from the module scikitlearn
iris = load_iris()

#Removing the one from each class for test data
removed = [0,50,100]
new_target = np.delete(iris.target,removed)
new_data = np.delete(iris.data,removed,axis=0)

classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(new_data,new_target)
prediction = classifier.predict(iris.data[removed])

print("Original target labels:",iris.target[removed])
f.write(str(iris.target[removed]))
f.write("\n")

print("Algorithm target labels:",prediction)
f.write(str(prediction))
f.write("\n")

from sklearn.metrics import accuracy_score
y_predict = classifier.predict(new_data)
print("Accuracy of the decision tree is : ",accuracy_score(new_target,y_predict))
f.write(str(accuracy_score(new_target,y_predict)))
f.write("\n")

#Create a dot data
graph_data = export_graphviz(classifier,out_file = None,feature_names=iris.feature_names,class_names = iris.target_names,filled=True,rounded=True,special_characters=True)

#graph = pydotplus.graph_from_dot_data(graph_data)
graph = pydotplus.graph_from_dot_data(graph_data)

#Display graph
graphtree = graphviz.Source(graph_data)
#graphtree.render("iris")

f.close()

#Adding the output in S3 bucket
s3 = boto3.client("s3")
s3.upload_file("DecisionTree_output.txt","demoiris","DecisionTree_output.txt")