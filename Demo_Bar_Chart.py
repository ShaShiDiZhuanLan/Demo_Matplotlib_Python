# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-4-29
UpdateTime: 2019-12-12
Info: matplotlib 使用示例 —— 柱形图
"""
import numpy as np
import matplotlib.pyplot as plt
#柱状图
A1 = [0.88,0.81,0.85]
A2 = [0.89,0.86,0.84]
A3 = [0.88,0.83,0.89]
A4 = [0.86,0.86,0.88]
A5 = [0.90,0.83,0.83]
x = np.arange(3) #总共有几组，就设置成几，我们这里有三组，所以设置为3
total_width, n = 0.6, 5    # n有多少个类型
width = total_width / n
x = x - (total_width - width) / 2
plt.bar(x, A1, color = "r",width=width,label='a1 ')
plt.bar(x + width, A2, color = "y",width=width,label='a2')
plt.bar(x + 2 * width, A3 , color = "c",width=width,label='a3')
plt.bar(x + 3 * width, A4 , color = "g",width=width,label='a4')
plt.bar(x + 4 * width, A5 , color = "b",width=width,label='a5')
plt.xlabel("横轴的名字")
plt.ylabel("纵轴的名字")
plt.legend(loc = "best")
plt.xticks([0,1,2],['左边','中间','右边'])
plt.ylim((0.8, 0.95))
my_y_ticks = np.arange(0.8, 0.95, 0.02)
plt.yticks(my_y_ticks)
plt.rcParams['font.sans-serif']=['SimHei']  # 中文
plt.show()