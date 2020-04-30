# -*- coding: utf-8 -*-
# author: ColinPython_榴莲老师
# 关注微信公众号：“ 青联科创 ”获得等多有趣代码教程
# 日期:2020-4-28,使用的工具:PyCharm,文件名:角度

import turtle

turtle.fd(100)  # 第一笔

turtle.left(90)
t = turtle.heading()
print(t)
turtle.fd(100)  # 第二笔


turtle.degrees(360.0)
t = turtle.heading()
print(t)
turtle.fd(100)  # 第三笔


turtle.degrees(720.0)
t = turtle.heading()
print(t)
turtle.fd(100)  # 第四笔

turtle.left(100)
turtle.fd(100)

turtle.done()
