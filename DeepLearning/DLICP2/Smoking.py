# Importing Required packages
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import xlrd

# Define the data set of housing details
DATA_FILE = 'data/Smoking.xls'

# Reading data from the .xls file using xlrd
# Reference : http://www.lexicon.net/sjmachin/xlrd.html
book = xlrd.open_workbook(DATA_FILE, encoding_override="utf-8")

# Making sure that index is starting from 0
sheet = book.sheet_by_index(0)

# Define an array with column values HouseAge and price from xls file
# Reading only Required Columns by Index
#data = np.asarray([[sheet.row_values(i)[1],sheet.row_values(i)[5]] for i in range(1, sheet.nrows)])
# avg price vs room
data = np.asarray([[sheet.row_values(i)[0],sheet.row_values(i)[1],sheet.row_values(i)[3]] for i in range(1, sheet.nrows)])
n_samples = sheet.nrows - 1
print(data)

# Create placeholders for input X (Avg. Age House Age) and label Y (Price)
# X = tf.placeholder(tf.float32, name='X')
X1 = tf.placeholder(tf.float32, name='Smoking')
X2 = tf.placeholder(tf.float32, name='Age')
Y = tf.placeholder(tf.float32, name='Number')

# Create weight and bias, initialized to 0
w1 = tf.Variable(0.0, name='weights')
w2 = tf.Variable(0.0, name='weights')

b = tf.Variable(0.0, name='bias')

# Build model to predict Y
Y_predicted = X1 * w1 + X2 * w2 + b

# Use the square error as the loss function
loss = tf.square(Y - Y_predicted, name='loss')

# Gradient descent with learning rate of 0.01 to minimize loss
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0001).minimize(loss)

with tf.Session() as sess:
    # Step 7: initialize the necessary variables, in this case, w and b
    sess.run(tf.global_variables_initializer())

    writer = tf.summary.FileWriter('./graphs/linear_reg', sess.graph)

    # Step 8: train the model
    for i in range(10):  # train the model 50 epochs
        total_loss = 0
        for x1, x2, y in data:
            # Session runs train_op and fetch values of loss
            _, l = sess.run([optimizer, loss], feed_dict={X1: x1,X2: x2, Y: y})
            total_loss += l
        print('Epoch {0}: {1}'.format(i, total_loss / n_samples))

    # close the writer when you're done using it
    writer.close()

    # Step 9: output the values of w and b
    w1,w2, b = sess.run([w1,w2,b])

# plot the results
X1,X2, Y = data.T[0], data.T[1], data.T[2]
plt.plot(X2, Y, 'bo', label='Real data')
plt.plot(X2, X1 * w1 + X2 * w2 + b, 'r', label='Predicted data')
plt.legend()
plt.show()
