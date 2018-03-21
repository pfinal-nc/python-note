# -*- coding: UTF-8 -*-
from matplotlib import pyplot as plt 
import numpy as np  
x = np.arange(1,11)
y = 2 * x + 5
plt.title('这个我不会')
plt.xlabel('纵轴是个啥')
plt.ylabel('横轴我不知道')
plt.plot(x,y)
plt.show()