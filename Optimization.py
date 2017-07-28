
# coding: utf-8

# # Введение
# 
# В этом задании вы научитесь решать задачи оптимизации с помощью библиотеки SciPy. Сначала вы решите задачу поиска минимума функции с помощью одного из градиентных методов оптимизации, затем увидите отличия в работе градиентного метода и одного из методов глобальной оптимизации, а в заключение – найдете глобальный минимум негладкой функции, т.е. функции, у которой не всегда определен градиент.
# 
# Понимание задачи глобальной оптимизации и отличий градиентных методов, от методов, не использующих градиент, очень полезно в задачах анализа данных, в частности, для подбора параметров алгоритмов.

# In[57]:

import numpy as np
from scipy.optimize import minimize, differential_evolution
#import this for graphics
import matplotlib.pyplot as plt


# In[3]:

def f (x) :
    return np.sin(x / 5.) * np.exp(x / 10.) + 5 * np.exp(-x / 2.)


# ## Задача 1. Минимизация гладкой функции

# In[77]:

res1 = minimize(f, 2, method='BFGS')
print res1.x
print res1

res2 = minimize(f, 30, method='BFGS')
print res2.x
print res2

print round(f(4.13627628),2)
print round(f(25.88019321),2)


# ## Задача 2. Глобальная оптимизация

# In[79]:

res3 = differential_evolution(f, [(1,30)])
print res3.x
print round(res3.fun,2)


# ## Задача 3. Минимизация негладкой функции

# In[92]:

def h (x) :
    return int(np.sin(x / 5.) * np.exp(x / 10.) + 5 * np.exp(-x / 2.))


# In[95]:

t = np.linspace(0.75,30.25)
gr1 = []
for x in t:
    gr1.append(h(x))
plt.plot(t,gr1,'b') 
plt.show()


# In[94]:

res2 = minimize(h, 30, method='BFGS')
print res2.x
print round(res2.fun,2)

res3 = differential_evolution(h, [(1,30)])
print res3.x
print round(res3.fun,2)

