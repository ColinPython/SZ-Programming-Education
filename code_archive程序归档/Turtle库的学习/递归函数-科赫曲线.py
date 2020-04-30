# -*- coding: utf-8 -*-
# author: ColinPython_榴莲老师
# 关注微信公众号：“ 青联科创 ”获得等多有趣代码教程
# 日期:2020-4-28,使用的工具:PyCharm,文件名:递归函数-科赫曲线

import turtle
t = turtle.Pen()
t.pencolor('lightblue')
t.pensize(10)
# t.width(2)  # 设置画笔的粗细
t.speed(10)

def koch(order):  #定义函数     order 命令
    if order == 0:
        t.forward(15)
    else:
        koch(order-1)
        t.left(60)
        koch(order-1)
        t.right(120)
        koch(order-1)
        t.left(60)
        koch(order-1)
koch(0)

koch(6)
turtle.done()