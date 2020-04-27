# -*- coding: utf-8 -*-
# author: ColinPython_榴莲老师
# 关注微信公众号：“ 青联科创 ”获得等多有趣代码教程
# 日期:2020-4-27,使用的工具:PyCharm,文件名:绘制正方形

# 做一个海龟画图大全，缩短turtle为t
import turtle as t
import time

# 定义控制面板函数
# c = t.textinput('想画什么', '输入数字,0查看菜单')
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

square()