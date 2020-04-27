# -*- coding: utf-8 -*-
# author: ColinPython_榴莲老师
# 关注微信公众号：“ 青联科创 ”获得等多有趣代码教程
# 日期:2020-4-27,使用的工具:PyCharm,文件名:绘制玫瑰花

# 做一个海龟画图大全，缩短turtle为t
import turtle as t
import time

# 定义控制面板函数
# c = t.textinput('想画什么', '输入数字,0查看菜单')
t.color("brown", "yellow")  # 定义默认画笔颜色red，填充颜色黄色
t.shape('turtle')  # 定义画笔造型为小海龟
t.screensize(700, 500, "silver")  # 银色700*500画布
t.speed(10)  # 画笔速度，0-10，10最快


# 3.玫瑰花
def rose():
    t.penup()
    t.left(90)
    t.fd(200)
    t.pendown()
    t.right(90)
    # 花蕊
    t.fillcolor("red")
    t.begin_fill()
    t.circle(15, 180)
    t.circle(25, 110)
    t.left(50)
    t.circle(60, 45)
    t.circle(20, 170)
    t.right(24)
    t.fd(30)
    t.left(10)
    t.circle(30, 110)
    t.fd(20)
    t.left(40)
    t.circle(90, 70)
    t.circle(30, 150)
    t.right(30)
    t.fd(15)
    t.circle(80, 90)
    t.left(15)
    t.fd(45)
    t.right(165)
    t.fd(20)
    t.left(155)
    t.circle(150, 80)
    t.left(50)
    t.circle(150, 90)
    t.end_fill()
    # 花瓣1
    t.left(150)
    t.circle(-90, 70)
    t.left(20)
    t.circle(75, 105)
    t.setheading(60)
    t.circle(80, 98)
    t.circle(-90, 40)
    # 花瓣2
    t.left(180)
    t.circle(90, 40)
    t.circle(-80, 98)
    t.setheading(-83)
    # 叶子1
    t.fd(30)
    t.left(90)
    t.fd(25)
    t.left(45)
    t.fillcolor("green")
    t.begin_fill()
    t.circle(-80, 90)
    t.right(90)
    t.circle(-80, 90)
    t.end_fill()
    t.right(135)
    t.fd(60)
    t.left(180)
    t.fd(85)
    t.left(90)
    t.fd(80)
    # 叶子2
    t.right(90)
    t.right(45)
    t.fillcolor("green")
    t.begin_fill()
    t.circle(80, 90)
    t.left(90)
    t.circle(80, 90)
    t.end_fill()
    t.left(135)
    t.fd(60)
    t.left(180)
    t.fd(60)
    t.right(90)
    t.circle(200, 60)

rose()
t.done()