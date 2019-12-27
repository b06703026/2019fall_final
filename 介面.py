from tkinter import *

window = Tk()
window.title('臺大美食評分系統')
# 背景圖片
photo = PhotoImage(file="C:\\Users\\chopp\\Downloads\\bgimage.png")
w = photo.width()
h = photo.height()
window.geometry('%dx%d' % (w, h))
image = Label(window, image=photo)
image.pack()
#上半部
top_header = Label(window, text='請選擇權重：',
                   font='微軟正黑體', bg='white')
top_header.place(x=105, y=73)
# 權重欄位
class CreateSpinbox:
    def __init__(self, name, x1, x2):
        self.label = Label(window, text=name, font='微軟正黑體', bg='white')
        self.label.place(x=x1, y=73)
        self.spinbox = Spinbox(window, from_=0, to=1, increment=0.1,
                               bg='white', font='微軟正黑體', width=5)
        self.spinbox.place(x=x2, y=73)

taste = CreateSpinbox('美味',250, 300)
cp = CreateSpinbox('CP值',400, 450)
space = CreateSpinbox('環境', 550, 600)
service = CreateSpinbox('服務', 700, 750)
# 下半部
bottom_header = Label(window, text='以下為推薦您的餐廳：',
                      bg='white', font='微軟正黑體')
bottom_header.place(x=140, y=203)
# 結果欄位
class CreateVar:
    def __init__(self, y):
        self.var = StringVar()
        self.label = Label(window, textvariable = self.var,
                           bg='white', font='微軟正黑體')
        self.label.place(x=185, y=y)

one = CreateVar(274)
two = CreateVar(355)
three = CreateVar(436)
sequence = [one, two, three]
# 得到權重
def weight():
    global taste, cp, space, service
    result = list()
    for i in [taste, cp, space, service]:
        result.append(i.spinbox.get())
        i.spinbox.quit()
    return result
# 得到餐廳名單(還要再編輯)
def restaurants():
    """ Input: list()，會放函數weight()  Output: list() """
    result = ['小飯館兒', '小日子', '低GI']
    return result
# 按鈕啟動函數
def click():
    global sequence
    for i in range(len(sequence)):
        sequence[i].var.set(restaurants()[i])
# 按鈕
search_btn = Button(window, text='開始搜尋', command=lambda: click(),
                    bg='white', font='微軟正黑體')
search_btn.place(x=870, y=66)


window.mainloop()