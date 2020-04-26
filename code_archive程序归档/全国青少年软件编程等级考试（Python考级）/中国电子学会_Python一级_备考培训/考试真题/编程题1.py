# -*- coding: utf-8 -*-
# author: ColinPython_榴莲老师
# 关注微信公众号：“ 青联科创 ”获得等多有趣代码教程
# 日期:2020-4-26,使用的工具:PyCharm,文件名:编程题1

import turtle  # 导入绘图工具库

# 绘制圆脸

turtle.penup()  # 画笔抬起
turtle.goto(0, -200)  # 回到画大圆脸的初始位置
turtle.pendown()  # 落下画笔
turtle.circle(200)  # 一半径为200,圆心在画笔左边

# 左眼
turtle.penup()  # 画笔抬起
turtle.goto(-100, 50)  # 回到画左眼小圆的初始位置
turtle.pendown()  # 落下画笔
turtle.fillcolor('blue')  # 设置填充颜色为蓝色
turtle.begin_fill()  # 开始填充
turtle.circle(20)  # 画一半径为20的圆,圆心在画笔左边
turtle.end_fill()  # 填充结束

# 画右眼
turtle.penup()  # 笔抬起
turtle.goto(100, 50)  # 回到画右眼小的初始位置
turtle.pendown()  # 落下画笔
turtle.fillcolor('blue')  # 设置填充颜色为蓝色
turtle.begin_fill()  # 开始填充
turtle.circle(20)  # 一半径为20的圆,圆心在画笔左边
turtle.end_fill()  # 填充结束

# 鼻子
turtle.penup()  # 笔抬起
turtle.goto(0, 50)  # 回到画鼻子的初始位置
turtle.pendown()  # 落下画笔
turtle.circle(-50, steps=3)  # 画半径-50圆内切正三角形,心在画笔右边
# 嘴
turtle.penup()  # 画笔抬起
turtle.goto(-150, -70)  # 回到画嘴的初始位置左嘴角
turtle.pendown()  # 落下画笔
turtle.goto(0, -170)  # 移动到底画线
turtle.goto(150, -70)  # 移动到右嘴角画线

turtle.hidedone()  # 隐藏画笔
turtle.done()  # 停止笔等待关闭画布
