from gensim.models import word2vec
import csv

# 開啟 CSV 檔案
with open('C:\\Users\\user\\Desktop\\環境.csv', newline='', encoding = "utf_8") as csvfile:
     
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)

    # 以迴圈輸出每一列
    for row in rows :
        row[1] = row[1].split(",")
        print(row)