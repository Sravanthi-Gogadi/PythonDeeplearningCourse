# import the required packages for performing lineardiscriminantAnalysis and Logistic Regression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression

# importing the metrics from scikitlearn
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits

# loading digits dataset
data=load_digits()

# importing features from dataset
x=data.data

# import target for features
y=data.target

# print the shape of the dataset
print(data.data.shape)

# Splitting the data into train and test data
train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.2, random_state=12)

# LDA
ldamodel=LinearDiscriminantAnalysis()

# Logistic
logmodel=LogisticRegression()

# fitting and predicting the lda model
ldamodel.fit(train_x,train_y)
ldaprediction=ldamodel.predict(test_x)
print("Linear discriminant analysis accuracy is ", accuracy_score(ldaprediction, test_y))

# fitting and predicting the logistic regression model
logmodel.fit(train_x, train_y)
logprediction=logmodel.predict(test_x)
print("Logistic regression accuracy is ", accuracy_score(logprediction, test_y))