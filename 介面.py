from tkinter import *
import json

window = Tk()
window.title('公館美食評分系統')
# 背景圖片
photo = PhotoImage(file="C:\\Users\\chopp\\Downloads\\bgimage.png")
w = photo.width()
h = photo.height()
window.geometry('%dx%d' % (w, h))
image = Label(window, image=photo)
image.pack()
# 上半部
top_header = Label(window, text='請選擇權重：',
                   font='微軟正黑體', bg='white')
top_header.place(x=205, y=73)


# 權重欄位
class CreateSpinbox:
    def __init__(self, name, x1, x2):
        self.label = Label(window, text=name, font='微軟正黑體', bg='white')
        self.label.place(x=x1, y=73)
        self.spinbox = Spinbox(window, from_=0, to=1, increment=0.1,
                               bg='white', font='微軟正黑體', width=5)
        self.spinbox.place(x=x2, y=73)


taste = CreateSpinbox('美味', 350, 400)
cp = CreateSpinbox('CP值', 500, 550)
space = CreateSpinbox('環境', 650, 700)
service = CreateSpinbox('服務', 800, 850)
# 下半部
bottom_header = Label(window, text='以下為推薦您的餐廳：',
                      bg='white', font='微軟正黑體')
bottom_header.place(x=240, y=203)


# 結果欄位
class CreateVar:
    def __init__(self, x, y):
        self.var = StringVar()
        self.label = Label(window, textvariable=self.var,
                           bg='white', font='微軟正黑體')
        self.label.place(x=x, y=y)


one = CreateVar(285,270)
two = CreateVar(285,315)
three = CreateVar(285,360)
four = CreateVar(285,405)
five = CreateVar(285,450)
sequence = [one, two, three, four, five]


# 得到權重
def weight():
    global taste, cp, space, service
    result = list()
    for i in [taste, cp, space, service]:
        w = i.spinbox.get()
        result.append(float(w))
    return result


path = "C:\\Users\\chopp\\.PyCharmCE2019.2\\config\\scratches\\AllScore.txt"
with open(path, 'r') as file:
    AllScore = json.load(file)


# 得到餐廳名單
def restaurants(weight):
    global AllScore
    AllWeightedScore = dict()
    for i in AllScore.keys():
        score = 0
        for j in range(4):
            score += AllScore[i][j] * weight[j]
        AllWeightedScore[i.strip('11-20')] = score
    result = list()
    for i in range(5):
        for j in AllWeightedScore.keys():
            if AllWeightedScore[j] == max(AllWeightedScore.values()):
                result.append(j)
                AllWeightedScore.pop(j)
                break
    return result


# 按鈕啟動函數
def click():
    global sequence
    for i in range(5):
        sequence[i].var.set(restaurants(weight())[i])

# 按鈕
search_btn = Button(window, text='開始搜尋', command=lambda: click(),
                    bg='white', font='微軟正黑體')
search_btn.place(x=970, y=66)

window.mainloop()