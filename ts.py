import turtle, colorsys

screen = turtle.Screen()
screen.setup(900, 900)
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

for i in range(150):
    t.pencolor(colorsys.hsv_to_rgb(0.12 - i / 150 * 0.12, 1, 1))
    t.forward(i * 2.8)
    t.right(165)

# Diwali message
w = turtle.Turtle()
w.hideturtle()
w.penup()

# black box behind the text
w.goto(-230, -45)
w.color("gold", "black")
w.pensize(3)
w.pendown()
w.begin_fill()
for side in (460, 90, 460, 90):
    w.forward(side)
    w.left(90)
w.end_fill()
w.penup()

# text
w.goto(0, -30)
w.color("gold")
w.write("Happy Diwali!", align="center", font=("Arial", 40, "bold"))

turtle.done()