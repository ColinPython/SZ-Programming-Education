from turtle import *
from random import *


def onecloud():
    hideturtle()
    speed(0)
    pensize(6)
    pencolor("#b0e0e6")
    fillcolor("#b0e0e6")
    begin_fill()
    seth(7)
    for i in range(randint(18, 23)):
        speed(0)
        fd(i)
        left(1)
    seth(90)
    for n in range(3):
        speed(0)
        circle(25, 200)
        right(60)
    end_fill()


hideturtle()


def clouds():
    speed(0)
    for m in range(5):
        speed(0)
        x, y = randint(-50, 90), randint(90, 140)
        up()
        goto(x, y)
        down()
        onecloud()
    up()
    goto(0, 0)
    down()
    seth(0)


def ground():
    hideturtle()
    speed(0)
    for i in range(300):
        speed(0)
        pensize(randint(1, 3))
        x, y = randint(-260, 260), randint(-160, -50)
        r, g, b = -y / 280, -y / 280, -y / 280
        pencolor(choice(["#778899", "#2F4F4F", "#808000"]))
        penup()
        goto(x, y)
        down()
        fd(randint(25, 30))


def sun():
    hideturtle()
    for i in range(6):
        speed(0)
        up()
        goto(randint(-300, -190), randint(130, 170))
        down()
        pensize(25)
        pencolor('#f0e68c')
        for n in range(randint(18, 24)):
            speed('fast')
            fd(2)
            left(2)
            fd(4)
            right(2)
    up()
    goto(-290, 167)
    down()
    pensize(5)
    pencolor('gold')
    fillcolor('yellow')
    begin_fill()
    for i in range(12):
        speed(0)
        circle(15, 90)
        right(120)
    end_fill()


def rainbow():
    hideturtle()
    speed(0)
    up()
    pensize(2)
    goto(-480, -350)
    down()
    right(100)
    speed(0)
    for i in range(9):
        pencolor('#F41900')
        circle(1000)
        right(0.1)
    for i in range(9):
        pencolor('#FF9919')
        circle(1000)
        right(0.1)
    for i in range(9):
        pencolor('#FFFF19')
        circle(1000)
        right(0.1)
    for i in range(9):
        pencolor('#3CB371')
        circle(1000)
        right(0.1)
    for i in range(9):
        pencolor('#98FB98')
        circle(1000)
        right(0.1)
    for i in range(9):
        pencolor('#6495ED')
        circle(1000)
        right(0.1)
    for i in range(9):
        pencolor('#6A5ACD')
        circle(1000)
        right(0.1)


def dandelion(n):
    seth(90)
    pensize(2)
    pencolor('#191970')
    fd(2.5)
    pensize(n)
    pencolor('#004D66')
    fd(10)
    seth(150)
    pencolor('#FFB3CC')
    for i in range(9):
        speed(0)
        fd(11)
        backward(11)
        right(15)
    up()
    seth(0)
    down()
    pensize(1)


def dandelions():
    for i in range(15):
        speed(0)
        ls = [1, 1.5, 2]
        up()
        goto(randint(-250, 250), randint(-80, 150))
        down()
        dandelion(choice(ls))
        up()
        goto(0, 0)
        seth(0)
        down()


def kite():
    hideturtle()
    up()
    goto(50, -165)
    seth(0)
    down()
    pensize(1)
    pencolor('black')
    fillcolor('black')
    begin_fill()
    for i in range(9):
        speed(0)
        fd(i)
        left(1)
    seth(93)
    for i in range(13):
        speed(0)
        fd(i)
        left(1)
    seth(180)
    for i in range(6):
        speed(0)
        fd(i)
        right(1)
    seth(-97)
    for i in range(13):
        speed(0)
        fd(i)
        right(1)
    end_fill()
    up()
    goto(71, -77)
    down()
    pencolor('#87cefa')
    pensize(1)
    for i in range(9):
        speed(0)
        circle(-20, 50)
        circle(20, -50)
    up()
    goto(62, -147)
    down()
    pencolor('black')
    pensize(1)
    seth(40)
    for i in range(23):
        speed(0)
        fd(i)
        left(0.5)
    seth(-80)
    pencolor('plum')
    fillcolor('#dc143c')
    begin_fill()
    fd(20)
    left(120)
    fd(30)
    left(120)
    fd(20)
    end_fill()
    seth(-40)
    up()
    fd(15)
    down()
    pensize(3)
    for i in range(14):
        speed(0)
        fd(i)
        left(1)
    up()
    goto(0, 0)
    down()
    seth(0)
    pensize(1)


def grass():
    speed(0)
    for i in range(170):
        speed(0)
        pensize(randint(2, 4))
        y = randint(-200, -160)
        pencolor(choice(['#90ee90', '#228b22', '#32cd32', '#8fbc8f']))
        penup()
        goto(randint(-300, 300), y)
        seth(0)
        pendown()
        left(90)
        circle(-50, randint(40, 120))
        up()
        goto(0, 0)
        seth(0)
        pensize(1)
        pencolor('white')
        down()


def oneflower(x, y):
    hideturtle()
    up()
    goto(x, y)
    down()
    speed(0)
    pensize(3)
    colors = ['#ffdead', '#db7093']
    fillcolor('#dda0dd')
    begin_fill()
    for i in range(64):
        speed(0)
        circle(i / 16, 140)
        pencolor(colors[i % 2])
        right(90)
    end_fill()
    pencolor('#00ff33')
    fillcolor('#00ff33')
    begin_fill()
    pensize(2)
    seth(-90)
    circle(-100, 20)
    seth(135)
    circle(-60, 10)
    seth(-45)
    circle(60, 10)
    seth(45)
    circle(-60, 10)
    seth(-135)
    circle(-60, 15)
    end_fill()
    up()
    goto(0, 0)
    down()
    seth(0)


def flowers():
    for i in range(5):
        speed(0)
        oneflower(randint(-190, 190), randint(-190, -150))
    up()
    goto(0, 0)
    seth(0)
    pensize(1)
    pencolor('#ffffff')
    down()


def tree(length, level):
    speed(0)
    pensize(8)
    pencolor(choice(lstree))
    if level < 0:
        return
    fd(length)
    left(45)
    tree(0.6 * length, level - 1)
    right(90)
    tree(0.6 * length, level - 1)
    left(45)
    backward(length)
    return


def leaves():
    speed(0)
    hideturtle()
    pensize(1)
    pencolor('#00fa9a')
    for i in range(150):
        speed(0)
        up()
        goto(randint(-160, -55) + randint(0, 3),
             randint(20, 55) + randint(0, 2))
        down()
        fillcolor(choice(['#3CB371', '#7FFFAA', '#90EE90', '#32CD32']))
        begin_fill()
        circle(randint(15, 25), 60)
        left(120)
        circle(randint(15, 25), 60)
        end_fill()


hideturtle()
speed(0)
clouds()
sun()
rainbow()
dandelions()
ground()
kite()
grass()
flowers()
lstree = [
    'orange',
    'coral',
    'salmon',
    'black',
    'green',
    'violet',
    'grey',
    'gold',
    'pink',
    'darkgreen']
up()
goto(-100, -70)
down()
seth(90)
tree(70, 8)
leaves()
done()
