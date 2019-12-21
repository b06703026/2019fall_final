#!/usr/bin/env python
# coding: utf-8

# In[9]:



import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.stem import SnowballStemmer

def preprocess(x):
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize 
    from nltk.stem import SnowballStemmer
    Raw = open (x) ### Load text

    Raw_C = Raw.read()

    Raw_L =  Raw_C.lower()                           ### lowercase everything

    words_token = nltk.word_tokenize(Raw_L) ### tokenization

    words_token = [word for word in words_token if word.isalpha()] ###remove the punctuations

    stopwords = stopwords.words('english')

    MR_porter = SnowballStemmer('english')

    words_stop = [word for word in words_token if word not in stopwords]

    stemmed_word = [MR_porter.stem(word) for word in words_stop]
    
    return(stemmed_word)

stemmed_word = preprocess(r'C:\Users\User\Desktop\文字探勘\corpus\1.txt')

dic = {} 

for item in stemmed_word: 
    if (item not in dic): 
        dic[item] = 0

for keys in dic.keys():
    
    for doc in stemmed_word:
        
        if (keys in doc):
            dic[keys] += 1
            
        else:
            dic[keys] += 0
            
print(len(dic.keys()), file = open(r"C:\Users\User\Desktop\文字探勘\HW1.txt", "a"))
print(stemmed_word, file = open(r"C:\Users\User\Desktop\文字探勘\HW1.txt", "a"))

print(dic)


# In[4]:


import glob
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.stem import SnowballStemmer


file_list = glob.glob(os.path.join(os.getcwd(), r"C:\Users\User\Desktop\文字探勘\corpus", "*.txt"))

corpus = []

for file_path in file_list:
    with open(file_path) as f_input:
        corpus.append(f_input.read())

Uni = []
postdoc = []


for i in corpus:

    Raw_L =  i.lower()                           ### lowercase everything

    words_token = nltk.word_tokenize(Raw_L) ### tokenization

    words_token = [word for word in words_token if word.isalpha()] ###remove the punctuations

    stopWords = stopwords.words('english')

    MR_porter = SnowballStemmer('english')

    words_stop = [word for word in words_token if word not in stopWords]

    stemmed_word = [MR_porter.stem(word) for word in words_stop]
    
    postdoc.append(stemmed_word)
    Uni.extend(stemmed_word)

list(set(Uni))
print(Uni, file = open(r"C:\Users\User\Desktop\文字探勘\Uni.txt", "a"))


# In[8]:


dic = {} 

for item in Uni: 
    if (item not in dic): 
        dic[item] = 0

for keys in dic.keys():
    
    for doc in postdoc:
        
        if (keys in doc):
            dic[keys] += 1
            
        else:
            dic[keys] += 0
            
print(dic)
Freq = sorted(dic.items() ,  key=lambda x:x[0].lower())
f =open(r"C:\Users\User\Desktop\文字探勘\dictionary.txt", "w")
print ("{:<8} {:<15} {:<10}".format('t_index','term','df'),file =f)
for i in range(len(Freq)):
    print("{:<8} {:<15} {:<10}".format(i+1,Freq[i][0],Freq[i][1]),file=f)


# In[88]:


Freq = sorted(dic.items() ,  key=lambda x: x[1])
f =open(r"C:\Users\User\Desktop\文字探勘\dictionary.txt", "a")
print ("{:<8} {:<15} {:<10}".format('t_index','term','df'),file =f)
for i in range(len(Freq)):
    print("{:<8} {:<15} {:<10}".format(i+1,Freq[i][0],Freq[i][1]),file=f)


# In[101]:


import math

docfreq = []
docunit=[]

for t,terms in enumerate(postdoc) :
    
    for f in Freq:
        if (f[0] in terms):
            tf = terms.count(f[0])
            N =len(file_list)
            df = dic[f[0]]
            idf = math.log((N / df) ,10)
            tf_idf = tf * idf
        else:
            tf_idf = 0
        docfreq.append(tf_idf)
    sum_square = 0
    for i in docfreq:
        sum_square += i**2
        
    for i in docfreq:
        docunit.append(i/(sum_square**0.5))
    F = open(f"{t+1}.txt", "w")
    
    print ("{:<8} {:<15}".format('t_index','tf-idf'),file =F)
    
    for i in range(len(docunit)):
        print ("{:<8} {:<15}".format(i+1,docunit[i]),file = F)
    

# perdoc.append(docfreq)


# In[6]:


Freq


# In[1]:


a = dict()
a['1']=2
a['3']=3
len(a)


# In[ ]:





# In[ ]:


import json
import glob
import os
name = glob.glob(os.path.join(os.getcwd(), r"C:\\Users\\user\\Desktop\\10筆留言", "*.json"))
withoutpath = []
counter = 0
for i in range(len(name)) :
    withoutpath.append(os.path.splitext(name[i]))
for i in range(len(name)) :
    #print(i)
    with open(file = "%s"%(name[i]), mode = 'r', encoding='utf_8') as load_1:
        load_dict = json.load(load_1)
        # split_word = u"\uc6d0\ubcf8"
        text1 = []
        for j in range(len(load_dict['reviews'])):
            content = load_dict['reviews'][j]["text"]
            text1.append(content)
            with open(file = "%s,%s.txt" %(withoutpath[i][0],j), mode = "w", encoding = "utf_8") as new_1:
                for k in range(len(text1)):
                    counter += 1
                    new_1.write(text1[k])
                    text1 = []
                    if counter == 586 or counter == 1172 :
                        k = input()


# In[29]:


import os
name = glob.glob(os.path.join(os.getcwd(), r"C:\\Users\\user\\Desktop\\10筆留言", "*.json"))
print(name)


# In[15]:


name[0]


# In[19]:


load_1 = json.load(name[0])


# In[20]:


name[0]


# In[21]:


print(load_1)


# In[22]:


load_dict = json.load(load_1)


# In[30]:


with open(file = '%s'%(name[0]), mode = 'r') as load_1:
    load_dict = json.load(load_1)


# In[26]:


file = '%s'%(name[0])


# In[27]:


file


# In[33]:


print(len(name))


# In[8]:


import json
import glob
import os
name = glob.glob(os.path.join(os.getcwd(), r"C:\\Users\\user\\Desktop\\10筆留言", "*.json"))
withoutpath = []
for i in range(len(name)) :
    withoutpath.append(os.path.splitext(name[i]))
for i in range(len(withoutpath)) :
    print(withoutpath[i][0])


# In[3]:


import glob
import os
name = glob.glob(os.path.join(os.getcwd(), r"C:\\Users\\user\\Desktop\\10筆留言", "*.json"))


# In[5]:


print(name[57])


# In[9]:


import json
import glob
import os
name = glob.glob(os.path.join(os.getcwd(), r"C:\\Users\\user\\Desktop\\10筆留言", "*.json"))
withoutpath = []
for i in range(len(name)) :
    withoutpath.append(os.path.splitext(name[i]))
for i in range(len(withoutpath)) :
    print(withoutpath[i][0])
    print(i)


# In[ ]:




