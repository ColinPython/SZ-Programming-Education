# -*- coding: utf-8 -*-
# author: ColinPython_榴莲老师
# 关注微信公众号：“ 青联科创 ”获得等多有趣代码教程
# 日期:2020-4-24,使用的工具:PyCharm,文件名:你好，世界！

import turtle

turtle.tracer(100)


def skip(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def H(color):
    turtle.color(color)
    skip(-300 + 5, 100)
    turtle.right(90)
    turtle.fd(100)
    skip(-300 + 5, 50)
    turtle.left(90)
    turtle.fd(40)
    skip(40 - 300 + 5, 100)
    turtle.right(90)
    turtle.fd(100)
    turtle.left(90)


def E(color):
    turtle.color(color)
    skip(55 - 300 + 5, 25)
    turtle.fd(46)
    turtle.left(90)
    turtle.circle(23, 180 + 130)
    turtle.right(40)


def L(color1, color2):
    turtle.color(color1)
    skip(115 - 300 + 5, 100)
    turtle.right(90)
    turtle.fd(100)
    skip(140 - 300, 100)
    turtle.color(color2)
    turtle.fd(100)
    turtle.right(90)


def O(color):
    turtle.color(color)
    skip(180 - 300 + 5, 50)
    turtle.circle(25, 360)


def dot(color):
    turtle.color(color)
    skip(220 - 300 + 5, 0)
    turtle.left(60)
    turtle.fd(7)
    turtle.left(120)


def W(color):
    turtle.color(color)  # 这个W1.0的版本因为太宽，画布600*600显示不出全部，所以从60度改到30
    skip(240 - 300 + 5, 50)
    turtle.right(75)
    turtle.fd(48)
    turtle.left(150)
    turtle.fd(48)
    turtle.right(150)
    turtle.fd(48)
    turtle.left(150)
    turtle.fd(48)
    turtle.right(75)


def O2(color):
    turtle.color(color)
    skip(320 - 300 + 5, 50)
    turtle.circle(-25, 360)


def R(color):
    turtle.color(color)
    skip(360 - 300 + 5, 50)
    turtle.fd(8)
    turtle.right(90)
    turtle.fd(50)
    turtle.left(180)
    turtle.fd(40)
    turtle.right(60)
    turtle.fd(20)
    turtle.right(30)


def L2(color):
    turtle.color(color)
    skip(405 - 300 + 5, 100)
    turtle.right(90)
    turtle.fd(100)
    turtle.left(90)


def D(color):
    turtle.color(color)
    skip(470 - 300 + 5, 25)
    turtle.left(90)
    turtle.circle(25, 360)
    turtle.fd(75)
    turtle.left(180)
    turtle.fd(97)
    turtle.left(53)
    turtle.fd(5)
    turtle.right(53)


def Exclamation(color):
    turtle.color(color)
    turtle.pensize(8)
    skip(500 - 300 + 5, 100)
    turtle.fd(80)
    skip(500 - 300 + 5, 2)
    turtle.dot(10)


# turtle.setup(600,600,0,0)
turtle.pensize(11)

turtle.speed(1)
H('blue')
E('green')
L('purple', 'red')
O('yellow')
dot('grey')
W('#1abc9c')
O2('orange')
R('brown')
L2('pink')
D('#b0c4de')
Exclamation('#333')

turtle.hideturtle()
turtle.update()
turtle.done()
