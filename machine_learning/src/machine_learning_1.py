import matplotlib
import pandas  # 讀取csv用的
import wget
from matplotlib import pyplot as plt # 畫圖用的 內建沒有中文字體所以要另外下載
from matplotlib.font_manager import fontManager
from ipywidgets import interact  # 互動元件可以讓你調整參數 這個存python環境無法用
import tkinter as tk

path = "../resources/Salary_Data.csv"
data = pandas.read_csv(path)
# print(data)

# 線性 y = w * x + b
x = data["YearsExperience"]
y = data["Salary"]

#  用wget下載字體之後設定
# wget.download("https://github.com/GrandmaCan/ML/raw/main/Resgression/ChineseFont.ttf")
fontManager.addfont("ChineseFont.ttf")
matplotlib.rc('font', family="ChineseFont")

plt.scatter(x, y, marker="x", color="red", label="真實數據")  # marker, color可以設定
plt.title("年資-薪水")
plt.xlabel("年資")
plt.ylabel("月薪")


def plot_pred(w, b):
    y_pred = x * w + b
    plt.plot(x, y_pred, color="blue", label="預測線")
    plt.xlim([0, 12])  # 設定區間
    plt.ylim([-60, 140])  # 設定區間
    plt.legend()  # 顯示label
    plt.show()


plot_pred(10, 10)
# interact(plot_pred, w=(-100, 100, 1), b=(-100, 100, 1))  # 改成用互動元件 but互動元件在存python環境無法使用


# 用線跟點的距離來打分數




