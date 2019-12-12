# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-4-29
UpdateTime: 2019-12-12
Info: matplotlib 使用示例 —— 散点图
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0., 5., 0.2)
plt.xlabel('横轴名字')
plt.ylabel('纵轴名字')
plt.rcParams['font.sans-serif']=['SimHei']  # 中文
plt.plot(x, x, 'r--', x, x ** 2, 'bs', x, x ** 3, 'g^')
plt.show()