# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-4-29
UpdateTime: 2019-12-12
Info: matplotlib 使用示例 —— 折线图
"""
import matplotlib.pyplot as plt

#折线图
x = [5,7,11,17,19,25]#点的横坐标
k1 = [0.82,0.91,0.93,1.26,0.97,0.95]#线1的纵坐标
k2 = [0.89,1.22,1.94,1.57,1.43,0.93]#线2的纵坐标
plt.plot(x,k1,'s-',color = 'r',label="红线的名字")#s-:方形
plt.plot(x,k2,'o-',color = 'g',label="绿线的名字")#o-:圆形
plt.xlabel("横坐标名字")
plt.ylabel("纵坐标名字")
plt.legend(loc = "best")#图例
plt.rcParams['font.sans-serif']=['SimHei'] # 中文
plt.show()