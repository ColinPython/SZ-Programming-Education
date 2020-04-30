# -*- coding: utf-8 -*-
# author: ColinPython_榴莲老师
# 关注微信公众号：“ 青联科创 ”获得等多有趣代码教程
# 日期:2020-4-30,使用的工具:PyCharm,文件名:无限海景

import turtle

p = turtle.Pen()
p.speed(9999)
p.pensize(5)
p._tracer(False)

p.penup()  # 第一层
p.goto(-4, -470)
p.pendown()
p.pencolor('red')
p.fillcolor('red')
p.begin_fill()
p.circle(670)
p.end_fill()

p.penup()  # 第二层
p.goto(0, -350)
p.pendown()
p.pencolor('orangered')
p.fillcolor('orangered')
p.begin_fill()
p.circle(550)
p.end_fill()

p.penup()  # 第三层
p.goto(0, -230)
p.pendown()
p.pencolor('darkorange')
p.fillcolor('darkorange')
p.begin_fill()
p.circle(430)
p.end_fill()

p.penup()  # 第四层
p.goto(0, -110)
p.pendown()
p.pencolor('orange')
p.fillcolor('orange')
p.begin_fill()
p.circle(310)
p.end_fill()

p.penup()  # 第五层
p.goto(0, 10)
p.pendown()
p.pencolor('gold')
p.fillcolor('gold')
p.begin_fill()
p.circle(190)
p.end_fill()

p.penup()  # 第六层
p.goto(0, 130)
p.pendown()
p.pencolor('yellow')
p.fillcolor('yellow')
p.begin_fill()
p.circle(70)
p.end_fill()

p.pencolor('teal')  # 第七层
p.penup()
p.goto(-650, 200)
p.pendown()
p.fillcolor('teal')
p.begin_fill()
for i in range(22):
    p.forward(1)
    p.right(1)
for i in range(14):
    for i in range(44):
        p.forward(1)
        p.left(1)
    for i in range(44):
        p.forward(1)
        p.right(1)
for i in range(44):
    p.forward(1)
    p.left(1)
for i in range(22):
    p.forward(1)
    p.right(1)
p.forward(4)
p.right(90)
p.forward(562)
p.right(90)
p.forward(1294)
p.right(90)
p.forward(562)
p.end_fill()

p.right(90)  # 第八层
p.pencolor('turquoise')
a = 180
for i in range(8):
    p.penup()
    p.goto(-650, (a))
    p.pendown()
    for i in range(22):
        p.forward(1)
        p.right(1)
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.right(1)
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.right(1)
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.right(1)
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.right(1)
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.right(1)
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.right(1)
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.right(1)
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.right(1)
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.right(1)
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.right(1)
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.right(1)
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.right(1)
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.right(1)
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.right(1)
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.left(1)
    p.pendown()
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.forward(4)
    a -= 70
b = 145
for i in range(7):
    p.penup()
    p.goto(-650, (b))
    p.pendown()
    p.penup()
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.left(1)
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.left(1)
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.left(1)
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.left(1)
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.left(1)
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.left(1)
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.left(1)
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.left(1)
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.left(1)
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.left(1)
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.left(1)
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.left(1)
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.left(1)
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.left(1)
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.penup()
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.pendown()
    for i in range(44):
        p.forward(1)
        p.left(1)
    for i in range(22):
        p.forward(1)
        p.right(1)
    p.forward(4)
    b -= 70

turtle.update()
turtle .done()
