import json
import requests
import glob
import os
import nltk
import jieba
import jieba.posseg as pseg
import codecs
from nltk.corpus import stopwords 
 
CorpusRoot = r"C:\\Users\\acer\\Desktop\\project\\stores"
file_list = glob.glob(os.path.join(os.getcwd(), CorpusRoot, "*.json"))

AllCorpus = []
CorpusPerReview = dict()
CorpusPerVendor = dict()
for file_path in file_list:
    BaseName = file_path.split('\\')[-1].strip('.json')
    with open(file_path,encoding = 'utf-8') as load_test:
        doc =json.load(load_test)

        CorpusPerReviewTemp = []
        CorpusPerVendorTemp= []
        AvgRate = 0
        Rate = None
        if len(doc['reviews']) != 0:
            for i in range(len(doc['reviews'])):
                Rate = float(doc['reviews'][i]['rating'])
                AvgRate += Rate
                TextRaw = doc['reviews'][i]['text']

                if '(원본)' in TextRaw :
                    TextChinese = TextRaw.split('(원본)')[-1]
                else:
                    TextChinese = TextRaw

                TextChineseRemoveN = TextChinese.replace('\n','')
                CorpusPerReviewTemp.append([Rate,TextChineseRemoveN])
                CorpusPerVendorTemp.append(TextChineseRemoveN)
            AvgRate = AvgRate / len(doc['reviews'])     
            CorpusPerVendor[BaseName] = [AvgRate,CorpusPerVendorTemp] 
            CorpusPerReview[BaseName] = "".join(CorpusPerVendorTemp)
            AllCorpus.extend(CorpusPerVendorTemp)
        else:
            pass
AllCorpus = ".".join(AllCorpus)

with open(file = "test5.txt", mode = "w", encoding = "utf_8") as new_1:
    for k in AllCorpus:
        new_1.write(k)

# 引用詞庫
jieba.load_userdict('C:\\Users\\acer\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\jieba\\dict2.txt')   

# 存停用詞, 分詞, 過濾後分詞的list
stopWords=[]
segments=[]
remainderWords=[]

# 讀入停用詞檔
with open('C:\\Users\\acer\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\jieba\\stop.txt', 'r', encoding='UTF-8') as file:
    for data in file.readlines():
        data = data.strip()
        stopWords.append(data)

# 讀入文件檔, 進行中文斷詞
with open('C:\\Users\\acer\\Desktop\\project\\test5.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    segments = jieba.cut(text, cut_all = False)

# 移除停用詞及跳行符號
remainderWords = list(filter(lambda a: a not in stopWords and a != '\n', segments))

# 印出過濾後的分詞
with open(file = "test6.txt", mode = "w", encoding = "utf_8") as new_1:
    for k in remainderWords:
        new_1.write(k + " ")
		
# -*- coding: utf-8 -*-
import sys
from gensim.models import word2vec
from gensim import models

def main():
    # 設立模型
    sentences = word2vec.LineSentence("C:\\Users\\acer\\Desktop\\project\\test6.txt")
    model = word2vec.Word2Vec(sentences, window = 8, size = 100, min_count = 3)
    # 保存模型
    model.save("w2v_test.model")

if __name__ == "__main__":
    main()

# 調用模型
model = word2vec.Word2Vec.load("w2v_test.model")

# 選出最接近"輸入項目"的詞，topn:選出前topn組
# 用most_similar
target = input()
similar_list = model.most_similar(positive = target, topn = 30)
print(similar_list1)
# 用similar_by_word
similar_list2 = model.similar_by_word("服務", topn = 30)
print(similar_list2)
# 用most_similar & 用similar_by_word 結果一樣

