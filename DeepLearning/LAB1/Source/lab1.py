import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.python.framework import ops
import pandas as pd

ops.reset_default_graph()

# Create graph
sess = tf.Session()

# Read the data file
data = pd.read_csv('data.csv')

# Cleaning and modifying the data
data = data.drop('id',axis=1)

# Mapping Benign to 0 and Malignant to 1 
data['diagnosis'] = data['diagnosis'].map({'M':1,'B':0})

x_vals = np.array(data.iloc[:,1:31])
y_vals = np.array(data.iloc[:,0])

# Set for reproducible results
seed = 99
np.random.seed(seed)
tf.set_random_seed(seed)

# Split data into train/test = 80%/20%
train_indices = np.random.choice(len(x_vals), round(len(x_vals)*0.8), replace=False)
test_indices = np.array(list(set(range(len(x_vals))) - set(train_indices)))
x_vals_train = x_vals[train_indices]
x_vals_test = x_vals[test_indices]
y_vals_train = y_vals[train_indices]
y_vals_test = y_vals[test_indices]

# Normalize by column (min-max norm)
def normalize_cols(m):
    col_max = m.max(axis=0)
    col_min = m.min(axis=0)
    return (m-col_min) / (col_max - col_min)
    
x_vals_train = np.nan_to_num(normalize_cols(x_vals_train))
x_vals_test = np.nan_to_num(normalize_cols(x_vals_test))

###
# Define Tensorflow computational graph
###

# Hyperparameters
# RMS optimizer
learning_rate=0.01
num_steps = 2500


# Declare batch size
batch_size = 25
# Initialize placeholders
x_data = tf.placeholder(shape=[None, 30], dtype=tf.float32)
y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)

# Create variables for linear regression
A = tf.Variable(tf.random_normal(shape=[30,1]))
b = tf.Variable(tf.random_normal(shape=[1,1]))

# Declare model operations
model_output = tf.add(tf.matmul(x_data, A), b)

# Declare loss function (Cross Entropy loss)
loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=model_output, labels=y_target))

# Declare optimizer
my_opt = tf.train.RMSPropOptimizer(learning_rate)
train_step = my_opt.minimize(loss)

###
# Train model
###

# Initialize variables
init = tf.global_variables_initializer()

# Create a summary to monitor cost tensor
summa=tf.summary.scalar("loss", loss)
sess.run(init)

# Actual Prediction
prediction = tf.round(tf.sigmoid(model_output))
predictions_correct = tf.cast(tf.equal(prediction, y_target), tf.float32)
accuracy = tf.reduce_mean(predictions_correct)

# Training loop
loss_vec = []
train_acc = []
test_acc = []
# op to write logs to Tensorboard
summary_writer = tf.summary.FileWriter('./graphs/lab1/RMS', graph=tf.get_default_graph())
for i in range(num_steps):
    rand_index = np.random.choice(len(x_vals_train), size=batch_size)
    rand_x = x_vals_train[rand_index]
    rand_y = np.transpose([y_vals_train[rand_index]])
    sess.run(train_step, feed_dict={x_data: rand_x, y_target: rand_y})

    temp_loss,summary = sess.run([loss,summa], feed_dict={x_data: rand_x, y_target: rand_y})
    loss_vec.append(temp_loss)

    summary_writer.add_summary(summary, num_steps * batch_size + i)


    if (i+1)%300==0:
        print('Loss = ' + str(temp_loss))

###
# Display model performance
###

# Plot loss over time
plt.plot(loss_vec, 'k-')
plt.title('Cross Entropy Loss per Generation')
plt.xlabel('Generation')
plt.ylabel('Cross Entropy Loss')
plt.show()


