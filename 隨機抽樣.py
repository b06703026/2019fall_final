import json
import glob
import os
number = [661,835,1362,602,705,857,1198,133,119,1290,1280,914,1400,1554,207,1334,596,379,963,991,957,497,286,1712,1197,412,976,1245,1343,1240,267,930,1123,702,91,1297,48,825,1496,106,1095,601,1265,776,1131,1142,965,120,532,1599,660,257,1191,1509,916,1262,1370,1420,285,745,1072,579,951,870,1281,1054,1404,901,528,1451,357,1715,767,1472,1575,1321,86,150,405,121,333,949,1529,980,670,575,376,1503,508,1479,790,967,290,1284,90,1373,1709,1535,1219,1357]
name = glob.glob(os.path.join(os.getcwd(), r"C:\\Users\\user\\Desktop\\10筆留言", "*.json"))
text2 = []
counter = 0

for i in range(len(name)) :
    #print(i)
    with open(file = "%s"%(name[i]), mode = 'r', encoding='utf_8') as load_1:
        load_dict = json.load(load_1)
        # split_word = u"\uc6d0\ubcf8"
        text1 = []
        for j in range(len(load_dict['reviews'])):
            content = load_dict['reviews'][j]["text"]
            text1.append(content)
            for k in range(len(text1)):
                counter += 1
                if counter in number :
                    text2.append(text1)
                text1 = []
print(text2)