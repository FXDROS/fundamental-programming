import turtle as x 
import random
s = x.Screen()
y = int(s.textinput("Rotatng Colorful Squares and Disks","Please enter the side length of the first square [20-60]: "))
x.hideturtle()
if y <20 or y >60 :
    x.write('False Size', align = 'center', font = ('Arial', 30, 'normal'))
else :
    x.penup()
    x.setposition(-200,0)
    x.pendown()
    x.speed(25)

    for t in range (72) :
        x.color(random.random(),random.random(),random.random())
        x.begin_fill()
        x.forward(y)
        x.right(90)
        x.forward(y)
        x.right(90)
        x.forward(y)
        x.right(90)
        x.forward(y)
        x.right(95)
        y += 2
        x.end_fill()

    x.penup()
    x.setposition(250,0)
    x.pendown

    z = y*0.5

    for t in range (36) :
        x.color(random.random(),random.random(),random.random())
        x.begin_fill()
        x.circle(z)
        x.left(10)
        z -= 2
        x.end_fill()

    x.penup()
    x.setposition(0,-350)
    x.color('blue')
    x.pendown()
    x.write('There are 72 Squares and 36 Disks', align = 'center', font = ('Courier', 30, 'normal'))

x.exitonclick()
x.mainloop()
