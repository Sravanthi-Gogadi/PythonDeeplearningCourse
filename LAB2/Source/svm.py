from sklearn.svm import SVC
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split

irisdataset=datasets.load_iris() #loading iris dataset
x = irisdataset.data
y = irisdataset.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2   )
#splitting the data into testing and training sets with 80-20 rule
clf = SVC(kernel='linear') #applying SVM with linear kernel
y_pred = clf.fit(x_train,y_train).predict(x_test) #fitting the model and predicting y for a new test variable
print("Accuracy with linear kernel: "+str(metrics.accuracy_score(y_test, y_pred))) #calc accuracy
clfr = SVC(kernel='rbf') #applying SVM with rbf kernel
y_predict = clfr.fit(x_train,y_train).predict(x_test) #fitting the model and predicting y for a new test variable
print("Accuracy with RBF kernel: "+str(metrics.accuracy_score(y_test,y_predict)))  #calc accuracy