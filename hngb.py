import random
import turtle

d = []

p = turtle.Turtle()
p.shape("arrow")
p.speed(0)
p.color("DimGray")

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
t.color("OliveDrab")

win = turtle.Screen()
win.title("Snake")
win.bgcolor("white")
win.bgcolor("Khaki")
win.setup(width=800, height=600,startx=None, starty=None)


m = turtle.Turtle()
m.shape("arrow")
m.left(90)
m.speed(-1)
m.speed(0)
m.color("SandyBrown")
m.shapesize(5)
m.penup()
m.goto(-390, -390)

def ryk():
    if chek():
        d = [appp]
        appp.copy



appp = turtle.Turtle()
appp.shape("triangle")
appp.speed(-1)
appp.penup()
appp.color("Salmon")


def upapp():
    x = random.randint(-390, 390)
    y = random.randint(-390, 390)
    appp.goto(x, y)


def go():
    z = random.randint(-390, 390)
    s = random.randint(-390, 390)
    p.goto(z, s)


def w():
    t.forward(10)
    chek()



def s():
    t.backward(10)
    chek()


def d():
    t.right(15)
    chek()


def a():
    t.left(15)
    chek()


def c():
    t.clear()
    chek()

def r():
    t.penup()
    t.home()
    t.pendown()
    chek()


def chek():
    if t.distance(appp) < 20:
        upapp()



win.listen()
win.onkeypress(w, "w")
win.onkeypress(s, "s")
win.onkeypress(d, "d")
win.onkeypress(a, "a")
win.onkeypress(c, " ")
win.onkeypress(r, "q")
upapp()

win.mainloop()




