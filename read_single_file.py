import json
with open(file = "C:\\Users\\acer\\Desktop\\python\\6 期末報告\\1.json", mode = 'r') as load_1:
    load_dict = json.load(load_1)
    text1 = []
    for i in range(10) :
        content = load_dict['reviews'][i]["text"]
        text1.append(content)
    with open(file = "new_1.text", mode = "w", encoding = "utf_8") as new_1:
        for i in range(len(text1)) :
            new_1.write(text1[i])
        