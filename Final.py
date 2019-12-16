# coding=utf-8
"""
1.抓每家餐廳的評論
2.準備字典們(taste_dict, price_dict, environment_dict, service_dict)
3.斷詞並歸類
4.判斷正負面
5.根據使用者偏好算出新評分
"""

class Restaurant:
    def __init__(self, name, comments):
        """ Input: name跟comments為string """
        self.name = name
        self.comments = comments
        self.taste = list()
        self.price = list()
        self.environment = list()
        self.service = list()
        self.ratio = list()
        self.grade = 0

    def cut_sort(self, taste_dict, price_dict, environment_dict, service_dict):
        """ 用套件將self.comments進行中文斷詞並歸類，
            放到self.taste/price/environment/service
            Input: dict皆為裝著多個string的list
            Output: self.taste/price/environment/service皆為裝著多個string的list """

    def judge(self):
        """ 判斷正負面，並算出每個分類的 正負面詞語淨值/詞語總數 aka百分比例，
            放到self.ratio
            Output: self.ratio為裝著4個float的list """

    def calculate_grade(self, preference):
        """ 依據偏好決定權重，乘以self.ratio，滿分5分
            分數放到self.grade
            Input: preference為['美味', '價格', '環境', '服務'](順序不一定)
            Output: self.grade為float """


from tkinter import *

window = Tk()
window.title('公館美食評分系統')
header = Label(window, text='請排序您的偏好', font=('微軟正黑體', 20), height=2)
header.pack()

class CreateOption:
    def __init__(self, name):
        self.frame = Frame(window)
        self.frame.pack(side=TOP)
        self.label = Label(self.frame, text=name, font='微軟正黑體')
        self.label.pack(side=LEFT)
        self.var = StringVar(self.frame)
        self.var.set('請選擇')
        self.menu = OptionMenu(self.frame, self.var, '美味', '價格', '環境','服務')
        self.menu.pack(side=LEFT)

one = CreateOption('1')
two = CreateOption('2')
three = CreateOption('3')
four = CreateOption('4')

def preference():
    result = list()
    for i in [one, two, three, four]:
        result.append(i.var.get())
        i.frame.quit()
    return result

search_btn = Button(window, text='開始搜尋')
search_btn.pack()

photo = PhotoImage(file= "C:\\Users\\chopp\\Downloads\\map.png")
w = photo.width()
h = photo.height()
window.geometry('%dx%d' % (h, w))
image = Label(window, image=photo)
image.pack()


window.mainloop()
