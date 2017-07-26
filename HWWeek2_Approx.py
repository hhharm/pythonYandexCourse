
# coding: utf-8

# # Задача 2: аппроксимация функции
# https://www.coursera.org/learn/mathematics-and-python/programming/QySgp/linieinaia-alghiebra-skhodstvo-tiekstov-i-approksimatsiia-funktsii
# 
# f(x) = sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)

# In[55]:

#import numpy for matrix handling
import numpy as np
#improt scipy module for calculation
from scipy.linalg import solve
#import this for graphics
import matplotlib.pyplot as plt


# Разложение на многочлен первой степени (точки 1 и 15).

# In[73]:

x = 1.
value1 = np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)
x = 15.
value15 = np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)
a = np.array([[1, 1], [1, 15]])
b = np.array([value1, value15])
x1 = solve(a,b)

t = np.linspace(0.75,15.75)
gr1 = np.sin(t / 5) * np.exp(t / 10) + 5 * np.exp(-t / 2)
gr2 = x1[0] + x1[1] * t

plt.plot(t,gr1,'b') 
plt.plot(t,gr2,'r') 
plt.show()


# Разложение на многочлен второй степени (точки 1, 8 ,15).

# In[74]:

x = 8.
value8 = np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)
a = np.array([[1, 1, 1], [1, 8, 64], [1, 15, 15*15]])
b = np.array([value1, value8, value15])
x2 = solve(a,b)

gr3 = x2[0] + x2[1] * t + x2[2] * t * t

plt.plot(t,gr1,'b') 
plt.plot(t,gr2,'r')
plt.plot(t,gr3,'g')
plt.show()


# Разложения на многочлен третей степени (точки 1, 4, 10, 15).

# In[94]:

x = 4.
value4 = np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)
x = 10.
value10 = np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)
a = np.array([[1, 1, 1, 1], [1, 4, 16, 4 ** 3], [1, 10, 100, 1000], [1, 15, 15*15, 15**3]])
b = np.array([value1, value4, value10, value15])
x3 = solve(a,b)

gr4 = x3[0] + x3[1] * t + x3[2] * t * t + x3[3] * t ** 3

plt.plot(t,gr1,'b') 
plt.plot(t,gr2,'r')
plt.plot(t,gr3,'g')
plt.plot(t,gr4,'c')
plt.show()


# Write answer to the file. Check its content.

# In[95]:

f = open("submission-2.txt", 'w')
x3[:] = [round(el,2) for el in x3]

resStr = np.array_str(x3)
f.write(resStr [2:-1])
f.close()

get_ipython().system(u'cat "submission-2.txt"')

