import turtle as t
t.colormode(255)  # 参数cmode -- 数值 1.0 或 255 其中之一

t.fillcolor((255, 230, 146))
t.begin_fill()
t.pencolor((255, 230, 146))
t.circle(150, 360)
t.end_fill()
t.penup()
t.goto(-100, 200)
t.pendown()
t.pencolor((149, 95, 23))
t.left(350)
t.pensize(5)
t.forward(30)
t.right(130)
t.forward(35)
t.penup()
t.goto(90, 205)
t.pendown()
t.left(350)
t.forward(30)
t.right(240)
t.forward(35)
t.penup()
t.goto(0, 75)
t.pendown()
a = 1
for i in range(20):
    if 0 <= i < 5 or 10 <= i < 15:
        a = a + 0.8
        t.left(10)
        t.forward(a)
    else:
        a = a - 0.8
        t.left(10)
        t.forward(a)
t.penup()
t.goto(0, 75)
t.pendown()
t.left(190)
a = 1
for i in range(20):
    if 0 <= i < 5 or 10 <= i < 15:
        a = a + 0.8
        t.right(10)
        t.forward(a)
    else:
        a = a - 0.8
        t.right(10)
        t.forward(a)
t.penup()
t.goto(-60, 160)
t.pendown()
t.pencolor((255, 106, 106))
t.left(100)
t.forward(25)
t.penup()
t.goto(-75, 155)
t.pendown()
t.forward(24)
t.penup()
t.goto(-90, 155)
t.pendown()
t.forward(23)
t.penup()
t.goto(60, 160)
t.pendown()
t.forward(25)
t.penup()
t.goto(75, 155)
t.pendown()
t.forward(24)
t.penup()
t.goto(90, 155)
t.pendown()
t.forward(23)
