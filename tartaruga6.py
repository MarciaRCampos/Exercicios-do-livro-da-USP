import turtle

janela = turtle.Screen()
janela.bgcolor('lightblue')

lara = turtle.Turtle()
lara.pensize(6)
lara.color('red')
lara.shape('turtle')
lara.speed(2)

for n in range(5):
    lara.forward(170)
    lara.right(145)

janela.exitonclick()
