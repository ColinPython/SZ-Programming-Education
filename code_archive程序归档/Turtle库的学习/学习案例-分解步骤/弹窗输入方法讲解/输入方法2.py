# -*- coding: utf-8 -*-
# author: ColinPython_榴莲老师
# 关注微信公众号：“ 青联科创 ”获得等多有趣代码教程
# 日期:2020-4-30,使用的工具:PyCharm,文件名:输入方法2

import turtle
wn = turtle.Screen()
wn.screensize(800, 600, "green")

wn.title("我们来一起绘制五角星")
y = wn.numinput("Poker", "Your stakes:", 1000, minval=10, maxval=10000)

# turtle.numinput(title, prompt, default=None, minval=None, maxval=None)
# 参数
# title -- 字符串
# prompt -- 字符串
# default -- 数值 (可选)
# minval -- 数值 (可选)
# maxval -- 数值 (可选)

print(type(y))  # 类型 <class 'float'>
print()   # 打印出来是字符串类型

# 弹出一个对话框窗口用来输入一个数值。
# title 为对话框窗口的标题，
# prompt 为一条文本，通常用来描述要输入的数值信息。
# default: 默认值,
# minval:可输入的最小值,
# maxval:可输入的最大值。
# 输入数值的必须在指定的 minval .. maxval 范围之内，否则将给出一条提示，对话框保持打开等待修改。
# 返回输入的数值。如果对话框被取消则返回 None。: