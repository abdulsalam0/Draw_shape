import turtle

abdul_turtle = turtle.Turtle()
abdul_turtle.speed(1)

def DrawShape(length,angle_in_shape,num_sides,num_of_shapes):
    for x in range(num_sides):
        abdul_turtle.forward(length)
        if x == num_sides-1:
            break
        else:
            abdul_turtle.left(angle_in_shape)

DrawShape(100,90,4,0)
