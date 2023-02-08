
import turtle
import sys
import xml.dom.minidom

draw_scaleX = 500
draw_scaleY = 500
UNIT = 10


def main():
	# create a turtle
	t = turtle.Turtle()
	screen = t.getscreen()
	screen.screensize(canvwidth=1000, canvheight=1000)
	screen.tracer(0)
	


	## TODO: DRAW Y-AXIS (LINE & LABEL)
	y_min = 3.20
	y_max = 60.00 
	y_name = "microseconds"

	# obtain the step for "drawing scale" & "user scale"
	draw_step = draw_scaleY / UNIT
	user_step = (y_max - y_min) / UNIT

	# go to starting position to draw y-axis
	goto_start(t, face='y')

	# draw, number & label y-axis
	for i in range(UNIT+1):
		x = t.xcor()
		y = t.ycor()

		# write y-axis numbering
		t.penup()
		t.goto(x-30, y)
		t.write(f"{round(y_min + user_step * i, 2)}", align="left")

		# draw label line
		t.goto(x-10, y)
		t.pendown()
		t.goto(x+10, y)

		# get back to initial position
		t.penup()
		t.goto(x, y)
		t.pendown()

		# move to next position for labelling
		if i != UNIT:
			t.goto(x, y+draw_step)


	# write y-axis name
	t.penup()
	t.goto(t.xcor()-30, t.ycor()+20)
	t.write(f"{y_name}", align="left")	
	t.pendown()




	## TODO: DRAW X-AXIS (LINE & LABEL)
	x_min = 1000
	x_max = 200000
	x_name = "list size"

	# step for drawing scale & user scale
	draw_step_x = draw_scaleX / UNIT
	user_step_x = (x_max - x_min) / UNIT

	# go to starting position to draw x-axis
	goto_start(t)

	# draw x-axis line and label
	for i in range(UNIT+1):
		# current position
		x = t.xcor()
		y = t.ycor()

		# write x-axis numbering
		t.penup()
		t.goto(x-20, y-30)
		t.write(f"{round(x_min + user_step_x * i, 2)}", align="left")

		# write x-axis name
		if i == round(UNIT/2):
			t.goto(x-50, y-50)
			t.write(f"{x_name}")

		# draw the label line
		t.goto(x, y-10)
		t.pendown()
		t.goto(x, y+10)

		# go to initial position
		t.goto(x, y)

		# go to next label position
		if i != UNIT:
			t.goto(x+draw_step_x, y)

	# go to start position
	goto_start(t)




	## TODO: DRAW GRAPH POINTS
	# read the datapoints from data.xml
	dom = xml.dom.minidom.parse("data.xml")
	sequence_element = dom.getElementsByTagName("Sequence")[0]
	datapoint_elements = sequence_element.getElementsByTagName("DataPoint")
	for i in range(len(datapoint_elements)):
		# obtain initial (x, y)
		x_initial = datapoint_elements[i].attributes["x"].value
		y_initial = datapoint_elements[i].attributes["y"].value

		# convert x,y based on draw scale
		x_convert = convert_scale(float(x_initial), x_max, x_min, draw_scaleX)
		y_convert = convert_scale(float(y_initial), y_max, y_min, draw_scaleY)


		# get pencolor
		pen_color = sequence_element.attributes["color"].value

		# go to the position
		t.pencolor(pen_color)
		t.goto((-draw_scaleX/2)+x_convert, (-draw_scaleY/2)+y_convert)
		t.dot(5)



	## TODO: WRITE GRAPH TITLE
	


	## TODO: WRTITE SAME PROGRAM, BUT OBTAIN INFO FROM XML FILE


	## TODO: WRITE SAME PROGRAM, BUT IN AN OOP STRUCTURE WITH A FILE MENU OPTION


	## TODO: ANALYSE THEIR PLOT PROGRAM





	screen.update()
	# set the turtle screen to be 700x700
	screen.mainloop()



def goto_start(a_turtle, face='y'):
	a_turtle.penup()
	a_turtle.goto(-draw_scaleX/2, -draw_scaleY/2)
	a_turtle.pendown()

	if face=='x':
		a_turtle.setheading(90)
	else:
		a_turtle.setheading(0)



def convert_scale(value, maxi, mini, to):
	"""
		value: value in actual-scale to be convertey to draw-scale
		maxi:   maximum value in the actual-scale
		mini:   minimum value in the actual-scale
		to:    maximum value of the draw-scale

		draw scale    =  0   -> "to"
		actual scale  =  mini -> maxi
		formula       -> (value-mini) * "to" / (maxi-mini)

		first we shifted the actual scale backward, from mini to zero
				mini -> maxi   becomes   0 -> maxi-mini

		then we transform from that scale to:
				0 -> "to"

		"value" comes from the actual scale, it must be converted to
		the 0 -> maxi-mini scale. that is
				value  becomes (value-mini)

		

	"""

	result = ( (value - mini) * to ) / (maxi - mini)
	result = round(result, 2)

	return result



if __name__ == '__main__':
	main()

	# dom = xml.dom.minidom.parse("data.xml")
	# sequence_element = dom.getElementsByTagName("Sequence")[0]
	# datapoint_elements = sequence_element.getElementsByTagName("DataPoint")
	# for i in range(5):
	# 	print(datapoint_elements[i].attributes["y"].value)