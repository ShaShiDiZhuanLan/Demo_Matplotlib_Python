# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-4-29
UpdateTime: 2019-12-12
Info: matplotlib 使用示例 —— 饼图
"""
import matplotlib.pyplot as plt

# 饼图
data = {
    '中国': (130, '#7199cf'),
    '美国': (115, '#4fc4aa'),
    '日本': (60, '#ffff10'),
}
# 设置绘图对象的大小
fig = plt.figure(figsize=(8, 8))
cities = data.keys()
values = [x[0] for x in data.values()]
colors = [x[1] for x in data.values()]
ax1 = fig.add_subplot(111)
ax1.set_title('饼图')
labels = ['{}:{}'.format(city, value) for city, value in zip(cities, values)]

explode = [0.05, 0, 0] # 设置饼图的凸出显示
ax1.pie(values, labels=labels, colors=colors, explode=explode, shadow=True) # 画饼状图， 并且指定标签和对应的颜色  指定阴影效果

# plt.savefig('pie.jpg') # 保存成图片
plt.rcParams['font.sans-serif']=['SimHei']  # 中文
plt.show()