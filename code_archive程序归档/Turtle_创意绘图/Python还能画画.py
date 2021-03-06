# -*- coding: utf-8 -*-
# author: ColinPython_榴莲老师
# 关注微信公众号：“ 青联科创 ”获得等多有趣代码教程
# 日期:2020-4-25,使用的工具:PyCharm,文件名:Python还能画画

from turtle import *
tracer(False)


def computer():  # start from the most northwest corner of the computer.
    pensize(4)
    pencolor('blue')
    seth(10)
    circle(-500, 16)
    rt(90)
    fd(10)
    rt(90)
    circle(500, 14)
    lt(85)
    fd(85)
    rt(90)
    fd(15)
    rt(90)
    fd(90)
    rt(120)
    fd(90)
    seth(265)
    circle(500, 8)
    lt(88)
    circle(550, 9)
    seth(90)
    fd(60)
    lt(85)
    circle(500, 10)
    pu()
    seth(40)
    fd(79)
    seth(-63)
    pd()
    fd(52)
    pu()
    seth(-160)
    fd(147)
    seth(-22)
    pd()
    fd(63)
    pu()
    bk(20)
    seth(-120)
    pd()
    circle(17, 60)
    lt(30)
    circle(50, 50)
    lt(30)
    circle(17, 60)
    pu()
    lt(180)
    circle(-17, 60)
    seth(-40)
    pd()
    circle(-50, 40)
    seth(-160)
    circle(-100, 42)
    seth(90)
    circle(-50, 40)
    pu()
    left(180)
    circle(-50, 10)
    seth(-39)
    pd()
    circle(50, 70)


def square():  # the key on the keyboard,start from the most southeast corner of the computer.
    seth(110)
    fd(7)
    lt(90)
    fd(9)
    lt(90)
    fd(7)
    lt(90)
    fd(9)


def keyboard():  # start from the most southeast corner of the computer.
    pencolor('red')
    seth(110)
    fd(20)
    lt(90)
    fd(120)
    lt(110)
    fd(40)
    lt(73)
    fd(100)
    seth(100)
    pu()
    fd(5)
    pd()
    square()
    bk(9)
    square()
    bk(9)
    square()
    bk(9)
    square()
    bk(9)
    square()
    bk(9)
    square()
    bk(9)
    fd(45 + 9)
    lt(90)
    fd(7)
    square()
    bk(9)
    square()
    bk(9)
    square()
    pu()
    bk(18)
    lt(90)
    fd(7)
    pd()
    fd(7)
    lt(90)
    fd(35)
    lt(90)
    fd(7)
    lt(90)
    fd(35)
    pu()
    bk(44)
    pd()
    square()
    bk(9)
    square()
    fd(9)
    rt(90)
    fd(7)
    square()
    bk(9)
    square()
    fd(9)
    rt(90)
    fd(7)
    square()
    bk(9)
    square()


def programmer():  # start from the most southeast corner of the programmer.
    pencolor('purple')
    seth(90)
    fd(50)
    seth(45)
    circle(70, 10)
    pu()
    circle(70, 58)
    pd()
    circle(70, 202)
    seth(-100)
    circle(500, 10)
    pu()
    seth(70)
    fd(170)
    pd()
    seth(-90)
    fd(15)
    rt(80)
    fd(10)
    seth(25)
    pu()
    fd(45)
    pd()
    seth(-70)
    fd(15)
    seth(10)
    fd(10)
    pu()
    seth(-100)
    fd(15)
    seth(-175)
    pd()
    pensize(8)
    fd(1)
    pu()
    fd(40)
    pd()
    fd(1)
    pensize(4)
    seth(-30)
    pu()
    fd(20)
    pd()
    seth(-40)
    circle(13, 50)


def questionmark(theta):  # the beginning angle is theta
    pd()
    pensize(4)
    seth(theta)
    fd(6)
    circle(-8, 180)
    lt(60)
    pu()
    fd(12)
    pd()
    pensize(5)
    fd(1)
    pu()


computer()
pu()
seth(-170)
fd(65)
pd()
pensize(3)
keyboard()
pu()
seth(180)
fd(130)
pd()
pensize(3)
pencolor('black')
seth(20)
fd(237)
pu()
fd(114)
pd()
fd(40)
rt(50)
fd(60)
pu()
bk(60)
rt(130)
fd(220)
pd()
programmer()
pu()
seth(105)
fd(120)
questionmark(30)
seth(40)
fd(30)
questionmark(15)
seth(1)
fd(30)
questionmark(1)
seth(145)
fd(135)
pd()
pencolor('black')
penup()
goto(0, 80)
pendown()

write('人生苦短，我学Python', move=False, align="left", font=("华文中宋", 28, 'bold'))

pencolor('red')
penup()
goto(0, -250)
pendown()

write('深圳青少年编程教育', move=False, align="left", font=("华文中宋", 15, 'bold'))
ht()
update()
done()
