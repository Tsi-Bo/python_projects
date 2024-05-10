from turtle import Turtle, Screen
import random 

tim = Turtle()
tim.shape("turtle")
tim.color("BlueViolet")

dash_length = 10
tim.pensize(2)

# MAKE A SQUARE IN DOTTED LINES
# for i in range(4):
#     for i in range(10):
#         tim.forward(dash_length)
#         tim.penup()
#         tim.forward(dash_length)
#         tim.pendown()
#     tim.right(90)

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return(r, g, b)

# MAKE DIFFERENT SHAPES
shapes = 10
sides = 3
for i in range(shapes):
    tim.color(random_color())
    for i in range(sides):
        tim.forward(100)
        tim.right(360 / sides)
    sides +=1




# RADOM WALK
# for i in range(100):
#     tim.color(random_color())
#     tim.forward(20)
#     tim.right(random.choice([0, 90, 180, 270, 360]))

# Circle / SPIROGRAPH
# radius = 100
# tim.speed("fastest")
# def draw_spirograph(size_of_graph):
#     for iu in range(int(360 / size_of_graph)):
#         tim.color(random_color())
#         tim.circle(radius)
#         current_heading = tim.heading()
#         tim.setheading(current_heading + size_of_graph)
# tim.teleport(-100)
# # draw_spirograph(5)
# position = tim.pos()
# for i in range(10):
#     tim.dot(20)
#     tim.teleport(position)
#     position += 50
    









screen = Screen()

screen.exitonclick()
