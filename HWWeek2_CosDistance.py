
# coding: utf-8

# # Задача 1: сравнение предложений
# 
# Дан набор предложений, скопированных с Википедии. Каждое из них имеет "кошачью тему" в одном из трех смыслов:
# 
#  - кошки (животные)
#  - UNIX-утилита cat для вывода содержимого файлов
#  - версии операционной системы OS X, названные в честь семейства кошачьих
#  
# ## Задача — найти два предложения, которые ближе всего по смыслу к расположенному в самой первой строке.
# В качестве меры близости по смыслу мы будем использовать косинусное расстояние.

# In[61]:

#import regular expressions handling
import re
#import matrix library
import numpy as np
#import distance
from scipy.spatial import distance


# Open file, read it and separate each sentence into words.

# In[8]:

textFile = open('sentences.txt','r')
sentences = textFile.readlines()
for i in range(len(sentences)):
    sentences[i] = sentences[i].lower()
    #sentences[i] = re.split('[^a-z]', sentences[i]) - bad way to do this because of ' (apostrof)
    sentences[i] = re.split('[^a-z]+', sentences[i])
    #removes all empty entries in list
    sentences[i] = filter(None, sentences[i])
    


# Create dictionary with all words.

# In[44]:

dictionary = {}
counter = 0
for sentence in sentences:
    for word in sentence:
        if word not in dictionary.keys():
            dictionary[word] = counter
            counter += 1


# Create matrix NxM where N is number of sentences and M is number of words. (i,j) element is number of j word in i sentence.

# In[47]:

numOfSentences = len(sentences)
words = dictionary.keys()
numOfWords = len(words)
matrix = np.eye(numOfSentences, numOfWords)
for i in range(numOfSentences):
    for j in range(numOfWords):
        matrix[i][j] = sentences[i].count(words[j])


# Create array with distances between 0 and i sentence. Find indexes of 2 the most closest to the 0th sentences.

# In[64]:

distances = []
for i in range(numOfSentences):
    distances.append(distance.cosine(matrix[0], matrix[i]))
arr = np.array(distances)
#get three minimum elements indexes, ignore first because it distance of 0th with itself
result = arr.argsort()[1:3]


# Write the result into the file.

# In[74]:

resultFileName = 'submission-1.txt'
f = open(resultFileName, 'w')
resultStr = str(result[0]) + ' ' + str(result[1])
f.write(resultStr)
f.close()


# Test: check the content of the result file.

# In[76]:

get_ipython().system(u'cat submission-1.txt')

