# -*- coding: utf-8 -*-
# author: ColinPython_榴莲老师
# 关注微信公众号：“ 青联科创 ”获得等多有趣代码教程
# 日期:2020-4-26,使用的工具:PyCharm,文件名:熊本熊

import turtle as t
t.pensize(5)
t.speed(10)


def _circle(x, y, color, size):  # 定义一个函数
    t.setheading(0)
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(size)
    t.end_fill()


_circle(150, 250, "black", 50)
_circle(150, 260, "white", 35)
_circle(-150, 250, "black", 50)
_circle(-150, 260, "white", 35)

t.begin_fill()
t.fillcolor("black")
t.up()
t.goto(200, 150)
t.down()
t.left(90)
t.circle(200, 180)
print(t.pos())
t.goto(-200, -150)
t.circle(200, 180)
t.goto(200, 150)
t.end_fill()
# 左手
t.up()
t.goto(200, 50)
t.down()
t.right(90)
t.begin_fill()
t.fillcolor("black")
t.fd(200)
t.left(90)
t.fd(50)
t.left(90)
t.fd(200)
t.end_fill()
t.up()
t.goto(420, 125)
t.down()
t.begin_fill()
t.fillcolor("black")
t.circle(50)
t.end_fill()
# 右手
t.up()
t.goto(-200, 50)
t.down()
t.begin_fill()
t.fillcolor("black")
t.fd(200)
t.right(90)
t.fd(50)
t.right(90)
t.fd(200)
t.end_fill()
t.up()
t.goto(-420, 25)
t.down()
t.begin_fill()
t.fillcolor("black")
t.circle(50)
t.end_fill()


# 鼻子
t.up()
t.goto(0, 25)
t.down()
t.begin_fill()
t.circle(110)
t.fillcolor("white")
t.end_fill()
t.up()
t.goto(0, 150)  # 鼻头
t.down()
t.begin_fill()
t.circle(20)
t.fillcolor("black")
t.end_fill()

# 腮红
t.up()
t.goto(-160, 80)
t.down()
t.begin_fill()
t.fillcolor("red")
t.circle(38)
t.end_fill()

t.up()
t.goto(160, 80)
t.down()
t.begin_fill()
t.fillcolor("red")
t.circle(38)
t.end_fill()

# 眼睛
t.up()
t.goto(-110, 200)
t.down()
t.begin_fill()
t.fillcolor("white")
t.circle(40)
t.end_fill()


t.up()
t.goto(110, 200)
t.down()
t.begin_fill()
t.fillcolor("white")
t.circle(40)
t.end_fill()

# 眼珠
t.up()
t.goto(-110, 240)
t.down()
t.circle(3)

t.up()
t.goto(110, 240)
t.down()
t.circle(3)

# 眉毛
t.setheading(-180)
t.up()
t.goto(-100, 290)
t.down()
t.pensize(2)
t.pencolor("white")
t.circle(60, 30)

t.setheading(-180)
t.up()
t.goto(120, 290)
t.down()
t.pensize(2)
t.pencolor("white")
t.circle(60, 30)

# 嘴
t.up()
t.goto(-45, 120)
t.down()
t.pencolor("black")
t.begin_fill()
t.fillcolor("black")
t.setheading(-90)
t.circle(50, 180)
t.end_fill()

t.done()
