
import turtle
import math



COLORS = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']



def main():

    # create turtle object & get turtle screen
    t = turtle.Turtle()
    screen = t.getscreen()
    screen.tracer(0)

    # draw rainbow
    draw_rainbow(t, 5)

    # draw smiley face
    draw_smiley_face(t, 15)








    # t.circle(50, 90)

    # t.penup()
    # t.goto(x, y)
    # t.setheading(0)
    # t.pendown()

    # t.circle(50, -90)

    screen.update()
    screen.mainloop()


def vanish_to(x, y, turtle_object):
    turtle_object.penup()
    turtle_object.goto(x, y)
    turtle_object.pendown()



def draw_rainbow(turtle_object, pen_size): 

    initial_heading = turtle_object.heading()
    initial_fill_color = turtle_object.fillcolor()
    initial_pen_size = turtle_object.pensize()
    initial_pen_color = turtle_object.pencolor()

    # obtain turtle current coordinate
    x = turtle_object.xcor()
    y = turtle_object.ycor()

    # allocate distance btw rainbow arcs and turtle current coordinate
    offset = 5*pen_size

    # place a dot at turtle current coordinate
    turtle_object.dot(3)

    # set turtle pen size
    turtle_object.pensize(pen_size)

    # draw the rainbow inner semi-circle TO outer semi-circle
    for i in range(7):

        # obtain semi-circle radius
        radius = (i * pen_size) + offset 

        # set pen color
        turtle_object.pencolor(COLORS[i])


        # go to semi-circle starting point (aim to draw anti-clockwise)
        vanish_to(radius * math.cos(0), radius * math.sin(0), turtle_object)
    

        # draw arc
        for j in range(1, 100):
            turtle_object.goto(radius * math.cos(j/100 * math.pi), radius * math.sin(j/100 * math.pi))

    # go to initial turtle location
    vanish_to(x, y, turtle_object)


    turtle_object.setheading(initial_heading)
    turtle_object.fillcolor(initial_fill_color)
    turtle_object.pensize(initial_pen_size)
    turtle_object.pencolor(initial_pen_color)





def draw_smiley_face(turtle_object, radius):
    ## TODO: DRAW SMILEY FACE 
    ##         - Face Structure
    ##         - Eye Structure
    ##         - Mouth Structure


    # obtain some initial properties of the turtle
    t = turtle_object
    x = t.xcor()
    y = t.ycor()

    initial_heading = t.heading()
    initial_fill_color = t.fillcolor()
    initial_pen_size = t.pensize()
    initial_pen_color = t.pencolor()


    # change the heading of turtle in favour of the "face drawing"
    t.setheading(0)
    t.pencolor("black")




    # face structure
    face_size = radius              # face circle radius

    t.fillcolor("yellow")           # face circle color
    t.begin_fill()

    # place turtle at starting
    # position to draw face circle
    vanish_to(x, y-face_size, t)

    # draw face circle
    t.circle(face_size)
    t.end_fill()

    # place turtle at initial position
    vanish_to(x, y, t)




    # eye structure
    eye_size = 12.5/100 * radius    # 12.5% of radius size (eye circle radius)
    eye_x = 35/100*radius           # 35% of radius size   
    eye_y = 15/100*radius           # 15% of radius size
    t.fillcolor("black")            # eye circle color


    # place turtle to draw left eye
    # relative to initial position
    vanish_to(x-eye_x, y+eye_y, t) 
    t.begin_fill()
    t.circle(eye_size) 
    t.end_fill()                                 


    # place turtle to draw righteye
    # relative to initial position
    vanish_to(x+eye_x, y+eye_y, t)  
    t.begin_fill()
    t.circle(eye_size) 
    t.end_fill()

    # place turtle back at initial position
    vanish_to(x, y, t)




    # # mouth structure
    mouth_size = 50/100 * radius     # 50% of radius size
    mouth_y = 50/100*radius          # 50% of radius size (below initial y_coordinate)
    mouth_draw_arc = 70
    mouth_pen_size = 5/100 * radius  # 5% of radius size

    # left arc of mouth
    t.pensize(mouth_pen_size)
    vanish_to(x, y-(50/100*radius),t)
    t.circle(mouth_size, 70)

    # right arc of mouth
    vanish_to(x, y-(50/100*radius),t)
    t.setheading(0)
    t.circle(mouth_size, -70)




    ## restore initial setting
    vanish_to(x, y, t)
    t.setheading(initial_heading)
    t.fillcolor(initial_fill_color)
    t.pensize(initial_pen_size)
    t.pencolor(initial_pen_color)
    


if __name__ == '__main__':
    main()