# imported required packages using sklearn and loading the scikit learn digits dataset
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import neighbors,datasets

#load digits dataset
dataset =datasets.load_digits()
#load data & target into x and y
x=dataset.data
y=dataset.target

# print the shape of the dataset
print(dataset.data.shape)

#split training & testing data into x and y with 20% testing data & 80%training data by applying a seed of value 9
train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.2, random_state=9)

# choose k values from 1 to 50
for i in range(1,51):
  #define the kmean model
  kmeanmodel=neighbors.KNeighborsClassifier(n_neighbors=i)
  #fit training data into kmeanmodel
  kmeanmodel.fit(train_x, train_y)
  #predict kmean for test data
  predict=kmeanmodel.predict(test_x)
  #calc the accuracy score using kmean model for different k values
  print("For K={} Accuracy is:{} ".format(i,accuracy_score(predict, test_y)))