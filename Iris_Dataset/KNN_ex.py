import boto3
from sklearn.datasets import load_iris
from sklearn import metrics

#Creating a file to store the output to the S3 bucket
f = open("KNN_output.txt","w+")

#Load the data from the module scikitlearn
iris = load_iris()

#Store features in x variable
x= iris.data

#Store response in y variable
y = iris.target

#Print the shape of x
print("Shape of x: ",x.shape)
f.write(str(x.shape))
f.write("\n")

#Print the shape of y
print("Shape of y:" ,y.shape)
f.write(str(y.shape))
f.write("\n")

#Steps of a Machine Learning model
#Step 1: Import the class Neighbors from sklearn for the KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier

#Step 2: Instantiating the estimator
est_inst = KNeighborsClassifier(n_neighbors=5)

print("Estimator for n=5 is:" ,est_inst)
f.write(str(est_inst))
f.write("\n")

#Step 3: Fit the model with data using x and y
est_inst.fit(x,y)

#Step 4: Predict the response for a new set of values
#est_inst.predict([3,5,4,2])

new = [[3,5,4,2],[5,4,3,2]]
est_inst.predict(new)

y_predict = est_inst.predict(x)
print("Accuracy of a model when n=5: ",metrics.accuracy_score(y,y_predict))
f.write(str(metrics.accuracy_score(y,y_predict)))
f.write("\n")

#list(iris.target_names)
#print(type(iris.data))
#type(iris.target)

#print(iris.data)
#print(iris.target)

#print(iris.target_names)
#print(iris.feature_names)

#Using the value n=1
est_inst = KNeighborsClassifier(n_neighbors=1)

print("Estimator for n=1: ",est_inst)
f.write(str(est_inst))
f.write("\n")

#Step 3: Fit the model with data using x and y
est_inst.fit(x,y)

#Step 4: Predict the response for a new set of values
#est_inst.predict([3,5,4,2])
y_predict = est_inst.predict(x)
print("Accuracy of a model when n=1: ",metrics.accuracy_score(y,y_predict))
f.write(str(metrics.accuracy_score(y,y_predict)))
f.write("\n")

est_inst.predict(new)
f.close()

#Adding the output in S3 bucket
s3 = boto3.client("s3")
s3.upload_file("KNN_output.txt","demoiris","KNN_output.txt")