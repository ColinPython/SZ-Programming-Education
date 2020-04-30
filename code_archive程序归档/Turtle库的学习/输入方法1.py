# -*- coding: utf-8 -*-
# author: ColinPython_榴莲老师
# 关注微信公众号：“ 青联科创 ”获得等多有趣代码教程
# 日期:2020-4-30,使用的工具:PyCharm,文件名:输入方法1|textinput

import turtle
wn = turtle.Screen()
wn.screensize(800, 600, "green")

t = wn.textinput("应用的标题title【创意绘图工具】", "请输入想绘制什么图形的名字")

# 函数源码讲解：👇
# turtle.textinput(title, prompt)
# 参数
# title -- 字符串
# prompt -- 字符串
# 弹出一个对话框窗口用来输入一个字符串。
# 形参 title 为对话框窗口的标题，prompt 为一条文本，通常用来提示要输入什么信息。返回输入的字符串。
# 如果对话框被取消则返回 None。

print(type(t))  # 类型 <class 'str'>
print(t)   # 打印出来是字符串类型




turtle.done()