import turtle

janela = turtle.Screen()
janela.bgcolor('blue')

Lara = turtle.Turtle()
Lara.pensize(6)

for cor in ['yellow', 'pink', 'black', 'red']:
    Lara.color(cor)
    Lara.forward(100)
    Lara.left(90)

janela.exitonclick()