import numpy as np
import matplotlib.pyplot as plt

x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([1,3,2,5,7,8,8,9,10,12])
xMean=np.mean(x)
yMean=np.mean(y)
B1=(np.sum((x-xMean)*(y-yMean)))/(np.sum(np.power((x-xMean),2)))
B0=yMean-(B1*xMean)
plt.scatter(x,y)
ry=B1*x+B0
plt.plot(x,ry)
plt.show()
