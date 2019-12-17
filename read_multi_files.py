import json
import glob
name = glob.glob(r'.\*.json')
for i in range(len(name)) :
    with open(file = "C:\\Users\\acer\\Desktop\\python\\6 期末報告%s"%(name[i]), mode = 'r') as load_1:
        load_dict = json.load(load_1)
        # split_word = u"\uc6d0\ubcf8"
        text1 = []
        for j in range(10):
            content = load_dict['reviews'][j]["text"]
            text1.append(content)
            with open(file = "test\\new%s.txt" %(j), mode = "w", encoding = "utf_8") as new_1:
                for k in range(len(text1)):
                    new_1.write(text1[k])
                    text1 = []