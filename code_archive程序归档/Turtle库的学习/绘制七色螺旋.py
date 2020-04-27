# -*- coding: utf-8 -*-
# author: ColinPython_榴莲老师
# 关注微信公众号：“ 青联科创 ”获得等多有趣代码教程
# 日期:2020-4-27,使用的工具:PyCharm,文件名:绘制七色螺旋


# 做一个海龟画图大全，缩短turtle为t
import turtle as t
import time

# 定义控制面板函数
# c = t.textinput('想画什么', '输入数字,0查看菜单')
t.color("brown", "yellow")  # 定义默认画笔颜色red，填充颜色黄色
t.shape('turtle')  # 定义画笔造型为小海龟
t.screensize(700, 500, "silver")  # 银色700*500画布
t.speed(10)  # 画笔速度，0-10，10最快


# 4.七彩螺旋
def spiral():
    colors = ['purple', 'orange', 'blue', 'green', 'silver', 'red', 'gold']
    t.bgcolor('black')
    for i in range(360):
        t.pencolor(colors[i % 7])
        t.pensize(1)
        t.width(i / 100 + 1)
        t.fd(i)
        t.right(50)

spiral()
t.done()