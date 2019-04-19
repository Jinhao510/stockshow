# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:33:14 2019

@author: Administrator
matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(1.0,5.0)
#print(x)
y1 = np.sin(np.pi*x)
y2 = np.sin(np.pi*x*3)


plt.subplot(221)
plt.plot(x,y1,'b--')
plt.subplot(222)
plt.plot(x,y2,'r--')
plt.subplot(223)
plt.plot(x,y1*2,'-o')
plt.subplot(224)
plt.plot(x,y2*2,'m-')


plt.show()