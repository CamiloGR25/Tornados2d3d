import turtle

ventana=turtle.Screen()
ventana.bgcolor("black")

#linea
linea=turtle.Turtle()
linea.speed(0)
linea.color("white")

figura=800

for i in range(figura):
    linea.forward(i*3)
    #tortuga.right(75)
    linea.right(145)

ventana.exitonclick()


