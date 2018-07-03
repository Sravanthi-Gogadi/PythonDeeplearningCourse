# import the required library numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt
# Given the features X and Y
x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([1,3,2,5,7,8,8,9,10,12])
# calculate the mean of X
xMean=np.mean(x)
# calculate the mean of y
yMean=np.mean(y)
# to calculate the coefficient of equation y = mx + c where B1 is the slope
B1=(np.sum((x-xMean)*(y-yMean)))/(np.sum(np.power((x-xMean),2)))
# calculate the y intercept of the linear equation y=mx+c where c is intercept of y
B0=yMean-(B1*xMean)
# plot the x and y values
plt.scatter(x,y)
# linear regression equation with b1 as slope and b0 as y intercept
ry=B1*x+B0
# plot the line that best separates the data points
plt.plot(x,ry)
# show the plot for the linear regression model
plt.show()
