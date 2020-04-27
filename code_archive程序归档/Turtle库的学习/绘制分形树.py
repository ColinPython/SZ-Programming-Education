# -*- coding: utf-8 -*-
# author: ColinPython_榴莲老师
# 关注微信公众号：“ 青联科创 ”获得等多有趣代码教程
# 日期:2020-4-25,使用的工具:PyCharm,文件名:绘制分形树

import turtle


def tree(branchlen, t):  # 海龟t
    if branchlen > 5:  # 最小规模，0直接退出
        t.forward(branchlen)  # 画树干
        t.right(20)  # 右倾20度
        tree(branchlen - 15, t)  # 减小规模，树干减1
        t.left(40)  # 回左倾40度，即左20
        tree(branchlen - 15, t)  # 减小规模，树干减15  # 调用自身
        t.right(20)  # 回右倾20度，即回正
        t.backward(branchlen)  # 海龟回到原位置

# 注意海龟作图的次序
# 先画树干 ， 再画右树枝 ， 最后画左树枝：与递归函
# 数里的流程一致


def main():
    t = turtle.Turtle()  # 生成海龟
    myWin = turtle.Screen()
    t.left(60)  # 海龟位置调整
    t.penup()  # 海龟位置调整
    t.backward(100)  # 海龟位置调整
    t.pendown()  # 海龟位置调整
    t.pencolor('green')  # 海龟位置调整
    tree(75, t)  # 画树，树干长度75
    myWin.exitonclick()
    t.update()  # 跟新画面
    t.hideturtle()  # 隐藏画笔
    t.done()  # 绘画结束


main()
