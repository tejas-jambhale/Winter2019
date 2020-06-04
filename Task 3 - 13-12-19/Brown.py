
# coding: utf-8

# In[1]:

import nltk
nltk.download()


# 1. brown corpus
# 2. Inaugural speech
# 3. book corpus - frequency distribution can be done(most common words in textbook)

# In[2]:

from nltk.corpus import brown


# In[4]:

brown.categories()


# In[5]:

print(type(brown))


# In[10]:

brown.words(categories="adventure")[:100]


# In[11]:

len(brown.words(categories="adventure"))


# In[13]:

from nltk.corpus import inaugural


# In[15]:

inaugural.fileids()


# In[16]:

len(inaugural.fileids())


# In[19]:

inaugural.words(fileids='1861-Lincoln.txt')[:20]


# In[20]:

print(len(inaugural.words(fileids='1861-Lincoln.txt')))


# In[24]:

inaugural.words(fileids='2009-Obama.txt')[:5]


# In[22]:

print(len(inaugural.words(fileids='2009-Obama.txt')))


# In[26]:

from nltk.book import *


# In[27]:

texts()


# In[28]:

sents()


# In[31]:

f = FreqDist(text7)
print(f)


# In[32]:

f = FreqDist(text1)
print(f)


# In[36]:

f.most_common(10)


# In[40]:

c = FreqDist(inaugural.words(fileids='1977-Carter.txt'))
c.most_common(10)


# In[ ]:



