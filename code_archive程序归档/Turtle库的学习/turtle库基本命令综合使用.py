# -*- coding: utf-8 -*-
# author: ColinPython_榴莲老师
# 关注微信公众号：“ 青联科创 ”获得等多有趣代码教程
# 日期:2020-4-27,使用的工具:PyCharm,文件名:turtle库基本命令综合使用

# time
# 做一个海龟画图大全，缩短turtle为t
import turtle as t
import time

# 定义控制面板函数
c = t.textinput('想画什么', '输入数字,0查看菜单')
t.color("brown", "yellow")  # 定义默认画笔颜色red，填充颜色黄色
t.shape('turtle')  # 定义画笔造型为小海龟
t.screensize(700, 500, "silver")  # 银色700*500画布
t.speed(10)  # 画笔速度，0-10，10最快


# 1.正方形
def square():
    t.fillcolor("green")
    t.begin_fill()  # 颜色填充
    for i in range(4):  # 四边
        t.left(90)  # 左90度转
        t.fd(100)  # 前进100
    t.end_fill()  # 填充结束
    t.penup()  # 画笔抬起
    t.fd(100)  # 画笔向前100
    t.shape('circle')  # 画笔变成圆圈
    time.sleep(1)  # 暂停1秒
    t.goto(100, 100)  # 移动到100，100坐标
    time.sleep(1)
    t.hideturtle()  # 隐藏画笔，t.showturtle()为显示画笔


# 2.五角星
def pentagram():
    t.hideturtle()
    t.color("red")
    t.begin_fill()
    for i in range(5):
        t.fd(100)
        t.right(144)  # 五角星的角度
    t.end_fill()


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

# 5字符串螺旋
def strspiral():
    name = t.textinput("what you want to show", '输入')
    t.bgcolor('black')
    colors = ['green', 'silver', 'red', 'gold']
    for i in range(100):
        t.pencolor(colors[i % 4])
        t.penup()
        t.fd(i * 4)
        t.pendown()
        t.write(name, font=('Arial', int((i + 4) / 4), 'bold'))
        t.right(89)


if c == '1':
    square()
    t.done()
elif c == '2':
    pentagram()
    t.done()
elif c == '3':
    rose()
    t.done()
elif c == '4':
    spiral()
    t.done()
elif c == '5':
    strspiral()
    t.done()
elif c == '0':
    print("1.正方形", "2.五角星", "3.玫瑰花", "4.七彩螺旋", "5.字符串螺旋")
    c = t.textinput('想画什么', '输入数字')
    if c == '1':
        square()
        t.done()
    elif c == '2':
        pentagram()
        t.done()
    elif c == '3':
        rose()
        t.done()
    elif c == '4':
        spiral()
        t.done()
    elif c == '5':
        strspiral()
        t.done()
