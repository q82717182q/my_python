import matplotlib
import pandas  # 讀取csv用的
import wget
from matplotlib import pyplot as plt # 畫圖用的 內建沒有中文字體所以要另外下載
from matplotlib.font_manager import fontManager
from ipywidgets import interact  # 互動元件可以讓你調整參數 這個存python環境無法用

path = "../resources/Salary_Data.csv"
data = pandas.read_csv(path)
# print(data)

# 線性 y = w * x + b
x = data["YearsExperience"]
y = data["Salary"]

w = 10
b = 0
y_pred = w*x + b
cost = (y - y_pred)**2
print(cost.sum() / len(x))
