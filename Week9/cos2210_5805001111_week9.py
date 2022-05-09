import turtle

def draw():
    window = turtle.Screen()
    window.title("The Star!!!! | 5805001111")
    window.bgcolor("red")

    shape =  turtle.Turtle()
    shape.shape('circle')
    shape.pensize(4)
    shape.speed(1)
    shape.shapesize(5,5)

    shape.goto(0, 200)
    shape.goto(-150, -150) 
    shape.goto(200, 100) 
    window.bgcolor("pink")
    shape.goto(-200, 100) 
    shape.goto(150, -150) 
    shape.goto(0, 200)
    shape.end_fill()

    text =  turtle.Turtle()
    text.write('The Star', move=False, align='center', font=("Arial", 60, "normal"))

    shape.shapesize(0.1,0.1)
    window.bgcolor("purple")
    window.mainloop()

    window.exitonclick()


draw()