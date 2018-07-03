# import tensorflow package
import tensorflow as tf
# Enter the shape for matrics a and b
a = list(map(int, input("please enter the shape of matrices a and b").split()))
# Enter the range for the matrices
sm, la = map(int, input("please enter the range of numbers for a and b").split())
# using random function from tensorflow define a matrix of shape a
ip1 = tf.random_uniform(a, sm, la, dtype=tf.int32, seed=27)
# using random function from tensorflow define a matrix of shape b
ip2 = tf.random_uniform(a, sm, la, dtype=tf.int32, seed=9)
# creating a variable of matrices a and b
a = tf.Variable(ip1)
b = tf.Variable(ip2)
# Enter the shape of matrix c
sh1 = list(map(int, input("please enter the shape").split()))
# Enter the range of numbers for matrix c
sm1, la1 = map(int, input("please enter the range of numbers").split())
# using random function from tensorflow define a matrix of shape c
ip3 = tf.random_uniform(sh1, sm1, la1, dtype=tf.int32, seed=18)
# creating the variable c
c = tf.Variable(ip3)

# (a^2 + b)*c

# performing a^2
power = tf.pow(a, 2)
# performing a^2 +b
sum1 = tf.add(power, b)
# performing (a^2+b)*c
mul = tf.matmul(sum1, c)

# initializing the variables
init = tf.global_variables_initializer()
# creating a session object
with tf.Session() as sess:
    # session object method run is used to actually give the output of the performed operations
    sess.run(init)
    # printing the output of all the require values
    print("The matrix a is", sess.run(a))
    print("The matrix b is", sess.run(b))
    print("The matrix c is", sess.run(c))
    print(" The value of a^2", sess.run(power))
    print(" The value of a^2 + b", sess.run(sum1))
    print(" The value of (a^2 +b)*c ", sess.run(mul))
