# -*- coding: UTF-8 -*-
from matplotlib import pyplot as plt 
import numpy as np  

x = np.arange(1,11)
y = 2 * x + 5
plt.title('Demo')
plt.xlabel('x axis caption')
plt.ylabel('y axis caption')
plt.plot(x,y,"ob")
plt.show()
