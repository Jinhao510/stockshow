# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:20:27 2019

@author: Administrator
"""
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

import seaborn as sns
import matplotlib.pyplot as plt


x=np.linspace(1,14,100)
y1=np.sin(x)
y2=np.sin(x+2)*1.5


def splt():
    plt.plot(x,y1)
    plt.plot(x,y2)

#sns.set()  #重製圖表
sns.set_style('darkgrid')
#sns.set_context('poster')


splt()
plt.show()