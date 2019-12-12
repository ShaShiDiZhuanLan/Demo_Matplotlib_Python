# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-4-29
UpdateTime: 2019-12-12
Info: matplotlib 使用示例 —— 三维散点图
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


data = np.random.randint(0, 255, size=[50, 50, 50])
x, y, z = data[0], data[1], data[2]
ax = plt.subplot(111, projection='3d') # 创建一个三维的绘图工程
# 将数据点分成三部分画，在颜色上有区分度
ax.scatter(x[:10], y[:10], z[:10], c='y') # 绘制数据点
ax.scatter(x[10:20], y[10:20], z[10:20], c='r')
ax.scatter(x[30:40], y[30:40], z[40:50], c='g')
ax.set_zlabel('Z') # 坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.rcParams['font.sans-serif']=['SimHei']  # 中文
plt.show()