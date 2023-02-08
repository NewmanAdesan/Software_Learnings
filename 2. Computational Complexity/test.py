
import tkinter
import turtle


def main():
	# create a tkinter window
	root  = tkinter.Tk()

	# create a canvas widget
	my_canvas = tkinter.Canvas(root, width=200, height=200, bg="white")
	my_canvas.pack()


	# create a turtle, that draws on the "my_canvas"
	tim = turtle.RawTurtle(my_canvas)
	tim.penup()

	# add a mouse drag event handler to "turtle time"
	# turtle object goes to the mouse coordinate
	# turtle object writes (mouse coordinate) as text at that location
	tim.ondrag(lambda x,y: show_location(x, y, tim))

	root.mainloop()


def show_location(x, y, turtle_object):
	
	turtle_object.goto(x, y)
	turtle_object.write(f"{x}, {y}")
	




main()