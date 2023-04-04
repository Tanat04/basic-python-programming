import turtle
me = turtle.Turtle()

me.speed(100)
screen = turtle.Screen()
screen.bgcolor("#000000")

me.penup()
me.goto(-160, -150)
me.pendown()

def mysquare():
    for j in range(4):
        me.forward(200)
        me.left(90-3)

colours = ["#FF0000", "#FFFF33","#00ff00","#33FAFF","#0000CC","#7F00FF","#FF00FF","#00CC66"]

for b in range(9):
    for a in colours:
        me.color(a)
        mysquare()
    me.left(5)


me.hideturtle()
