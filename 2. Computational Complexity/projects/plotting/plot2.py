
import tkinter
import sys
import turtle
import xml.dom.minidom
import tkinter.filedialog
import math


def main ():

	root = tkinter.Tk()

	# this program accepts a command line argument; the xml plot file
	datafile = None 		
	if len(sys.argv) > 1:
		datafile = sys.argv[1]

	# WHAT IS "PlotApplication"? (GO-TO LINE 29)
	plot_app = PlotApplication(root, datafile)
	plot_app.mainloop()

	print("Program Execution Completed.")





class PlotApplication (tkinter.Frame):

	"""
		What is PlotApplication?

		1. PlotApplication is class which is a child of tkinter Frame object (tkinter frame widget)
		   meaning every object of this class is first and foremost a tkinter Frame widget


		2. on creation it accepts two argument, 
		   the window where it would dwell
		   the file it will work with

	"""


	def __init__(self, master=None, datafile=None):
		super().__init__(master)	# initialize itself as a frame (dwells in the "master" window)
		self.datafile = datafile 	# set the file as an attribute of the class
		self.pack()					# pack the frame unto the master; this function is inherited


		# THE "buildWindow" FUNCTION (GO-TO LINE *85 )
		self.buildWindow()	


	def buildWindow( self ):

		"""
			WHAT IS THE buildWindow" FUNCTION?
			----------------------------------

			1. we add a tkinter Canvas into the frame
			   this is the drawing space for our plot


			2. we place a turtle object unto the canvas widget
			   this turtle object will draw on the canvas widget


			3. we obtain the Screen object of the turtle
			   because we want the turtle screen to update on command.
			   the Screen Object tracer & update functions gives us this functionality


			4. if the PlotApplication was supplied a "datafile" upon creation
			   (by the way, the datafile is an xml file that specifies how the plot should look
			   that is the labelling, the datapoints) 

			   we are going to run the "datafile" through an engine, 
			   which is a function called "load_file(filename, turtle_obj)"

			   basically it obtains plot information from a data file passed to it
			   and using a turtle object also passed to it, 
			   draws the plot based on those plot information

		"""


		def buildWindow_main():

			# give the master window a title; this attribute is inherited 
			self.master.title("Plot")					

			# add a canvas to the left side of the frame (itself)
			canvas = tkinter.Canvas(self, width=1000, height=800) 	
			canvas.pack(side=tkinter.LEFT)

			# add a turtle object to the canvas
			turtle_obj = turtle.RawTurtle(canvas)

			# obtain the screen object of the turtle
			screen = turtle_obj.getscreen()

			# make it so, we control when the screen is updated
			screen.tracer(0)

			# load the plot file into the canvas
			if self.datafile != None:

				# THE "load_file" FUNCTION (GO-TO LINE )
				load_file(datafile=self.datafile.strip(), turtle_obj=turtle_obj) 


			## create a menu bar called "file" on the master window
			## this menu will have two items 
			## the first loads the plot file into view
			## the second exits the program (exit the master window)
			bar = tkinter.Menu(self.master)				# create a menu bar on the master window
			file_menu = tkinter.Menu(bar, tearoff=0)	# create a menu container in the menu bar, thIS will directly house the menu items



			"""
				two items will be placed in the menu container
				item-1 is "Load Plot Data ..."
				item-2 is "Exit"


				when item-1 is clicked a load_file function is called
				before looking through load_file function, 
				have an idea of all that goes on in "buildWindow_main"
				because load file will use some variables defined in "buildWindow_main" 

			"""
			file_menu.add_command(label="Load Plot Data ...", command=lambda t=turtle_obj: load_file(turtle_obj=t))
			file_menu.add_command(label="Exit", command=self.master.quit)		# second item in the menu container; it shuts down the master window

			bar.add_cascade(label="File", menu=file_menu)						# complete the configuration of the menu bar; its title, its menu container
			self.master.config(menu=bar)										# complete the configuration of the menu bar; adding it to the master window


		def load_file( filename=None, turtle_obj=None ):

			"""
				HOW EXACTLY DOES THE "load_file" FUNCTION WORK?
				-----------------------------------------------

				1. it accepts two keyword argument, a file name, and a turtle object,
				   "filename" & "turtle_obj". 


				2. in the case no argument was passed to the "filename"
				   a tkinter filedialog widget will be prompted so user can choose a file
				   the filedialog returns a file path selected
				   now we have a file name.


				3. the turtle object passed to load_file is a Raw Turtle on a Canvas.
				   we will instruct the turtle to draw on the Canvas.
				   first we set the turtle to it's initial state @ coordinate (0,0), then we update the screen
				   

				4. i will assume you are familiar with the layout of the xml file
				   we need to obtain the axis information of our plot;
				   the x & y axis attributes (label, min, max),
				   the plot title which will be the master window title.

				   from this information, we then obtain the size of the axes (max-min)
				   we also obtain the center of the axes.
				   we will soon see why this derived information are useful


				5. now think of our plot as a box right.
				   the length and breadth of that box will be size of x & size of y respectively
				   this is why we obtained the size of each axis

				   now think about the position of the box in a grid system.
				   what will be the coordinate of the box edges.
				   starting from the bottom-left edge, going anti-clockwise
				   you will agree with me that it would be 
				   (xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)

				   dont forget that in a plot, apart from the x-axis line & y-axis line & the graph
				   we also have labelling. that means we need to make our box slightly bigger,
				   we need clearance. 

				   lets choose a 40% clearance, 
				   such that the length of our box becomes x_size + 40% of x_size
				   such that we have 20% increase to the left x_min - 20% of x_size,
				   we have 20% increase to the right x_max + 20% of x_size

				   also the breadth of our box becomes y_size + 40% of y_size
				   such that we have 20% increase to the bottom y_min - 20% of y_size,
				   we have 20% increase to the top y_max + 20% of y_size

				   therefore our box of view becomes bigger


				6. we can specify the coordinate for our turtle screen
				   such that the coordinate of our turtle screen will be the box coordinate
				   our plot will lie in.

				   using the turtle screen "setworldcoordinate" function, 
				   we can specify the coordinate of our screen.

				   this functionality makes it very easy to instruct our turtle
				   to go to a specific coordinate


				7. time to draw the plot. this is divided into
					i) draw axes lines
					ii) draw axes title
					iii) draw axes numbering


				8. draw the axes lines:
				   we would move the turtle from the coordinate
				   (xmin, ymax) to (xmin, ymin) to (xmax, ymin)


				9. draw the axes title
				   x-axis title: at center of x-axis and 10% of ysize away from the ymin
				   y-axis title: at center of y-axis and 10% of xsize away from the xmin


				10. draw the axes numbering: 
					numbering a point on the axis is divided into 3 sections
				    i) the numbering short line
				    ii) the number itself
				    iii) the decimal place of the number

				
					i) the numbering short line
				          this is a short line perpendicular to the axis to be numbered
				       	  under this short line the actual number will be position

				          the x-axis numbering short line would be a vertical line 
				          that cuts through the x-axis perpendicularly
				          we will make the size of this line 5% of ysize
				          from 2.5% above the x-axis to 2.5% below the x-axis

				          the y-axis numbering short line woud be a horizontal line
				          that cuts through the y-axis perpendicularly
				          we will make the size of this line 5% of xsize
				          from 2.5% above the y-axis to 2.5% below the y-axis

					
					ii) the number itself
						  each axis will be divided into 10 equal places
						  each place would be numbered. 
						  that is every 10% of the xsize would be numbered. 

						  at that point, we would draw the short numbering line
						  and place the number exactly 5% away from the axis line

						  the numbering of the x-axis would be 5% of ysize below the x-axis
						  the numbering of the y-axis would be 5% of xize to the left of the y-axis

						  the actual number will be xmin + 


					iii) the decimal place of the number
							we are going to add a bit of responsiveness 
							to how much decimal places the numbering will show 
							based of the range/size of the axis

							this algorithm is pretty interesting.
							the main idea is this, 
							the more the range, the lesser the amount of decimal places that needs to be shown
							the less the range, the more the amount of decimal places that needs to be shown

							based on our design, 
							the highest decimal places for a numbering was made to be four(4)
							axis size in range (0 <= size < 10) would have the decimal place of 4 
							axis size in range (10 <= size < 100) would have the decimal place of 3
							axis size in range (100 <= size < 1000) would have the decimal place of 2
							axis size in range (1000 <= size < 10000) would have the decimal place of 1
							axis size in range (10000 <= size < 100000) would have the decimal place of 0
							axis size in range (100000 <= size < 1000000) would have the decimal place of -1

							since there is nothing like the decimal place of -1,-2,-3, ...
							we will cap it all at the decimal place of 0.

							we could use an if statement which would span quite the line of code
							OR we just take a "mathematical route".
							notice the relationship btw input=10 & output=3	which is 
							(10^1 = 10) & (4-1 = 3)
							(10^2 = 100) & (4-2 = 2)
							...             ...
							...             ...
							(10^5 = 100000)  &  (4-5 = -1)  &  max(-1, 0) = 0


							do you get it,
							if we can get how power of 10 would give the axis size we are done.
							we just substract that power from 4
							and would take the maximum between the answer & 0.
							the question now is "what mathematical syntax gives us that power"
							the answer is logarithm.


							math.log(10, 10) = 1         
							math.log(50, 10) = 1.698     -> math.floor(1.698) = 1   -> max(4-1, 0) = 1
							math.log(99, 10) = 1.995     -> math.floor(1.995) = 1
							math.log(100, 10) = 2
							math.log(500, 10) = 2.698    -> math.floor(2.698) = 2   -> max(4-2, 0) = 2
							math.log(990, 10) = 2.995    -> math.floor(2.995) = 2
							math.log(100000, 10) = 5
							math.log(500000, 10) = 5.698 -> math.floor(5.698) = 5   -> max(4-5, 0) = 0
							math.log(990000, 10) = 5.995 -> math.floor(2.698) = 2   


							now you get the algorithm workflow
							which can be done in just one line
							x_decimal_places = max(4-(math.floor(math.log(xsize, 10))), 0)
							y_decimal_places = max(4-(math.floor(math.log(ysize, 10))), 0)


				9. draw the sequence title & plot datapoint
				   in the plot file, 
				   apart from the axes information,
				   we have sequences information, whereby in a particular plot
				   there can be one or more sequences of datapoints that denotes a plot

				   so each sequence contains three things
					   i) sequence plot title
					   ii) sequence plot title color 
					   iii) sequence datapoints information


				   i) sequence plot title
						   each sequence plot title would be drawn 
						   in term of x-axis, at the center of the x-axis (xcenter)
						   in term of y-axis, they will be below each other. 
						   more specifically 10% of ysize below each other


				   ii) sequence plot title color
						   the title would be written in the color specified its color attributes


				   iii) sequence datapoints information
						   for each datapoint in the datapoints information
						   we will move the turtle to the datapoint location
						   and place a dot at that location. 
						   the dot would be drawn in the color specified by the sequence color attribute.


				   LET'S GET TO WORK


			"""


			# obtain a plot file
			if filename == None:
				filename = tkinter.filedialog.askopenfilename(title="Select a Plot file")

			# if no filename chosen
			if filename == "" or not filename:
				return

			# set turtle to initial state
			turtle_obj.clear()
			turtle_obj.penup()
			turtle_obj.goto(0, 0)
			turtle_obj.pendown()
			turtle_obj.color("black")

			# update the turtle screen
			screen = turtle_obj.getscreen()
			screen.update()					

			# obtain the plot tile, set as master window title
			xmldom = xml.dom.minidom.parse(filename)
			plot_element = xmldom.getElementsByTagName("Plot")[0]

			plot_element_attributes = plot_element.attributes
			plot_title = plot_element_attributes["title"].value
			self.master.title(plot_title)

			# obtain the x & y axis attributes (label, min, max)
			axes_element = plot_element.getElementsByTagName("Axes")[0]
			xaxis_element = axes_element.getElementsByTagName("XAxis")[0]
			yaxis_element = axes_element.getElementsByTagName("YAxis")[0]

			xaxis_element_attributes = xaxis_element.attributes
			yaxis_element_attributes = yaxis_element.attributes


			xlabel = xaxis_element.firstChild.data.strip()
			ylabel = yaxis_element.firstChild.data.strip()

			xmin = float( xaxis_element_attributes["min"].value )
			xmax = float( xaxis_element_attributes["max"].value )

			ymin = float( yaxis_element_attributes["min"].value )
			ymax = float( yaxis_element_attributes["max"].value )


			xsize = xmax - xmin
			xcenter = xmin + ((xmax - xmin) / 2.0)

			ysize = ymax - ymin
			ycenter = ymin + ((ymax - ymin) / 2.0)


			print(xmin, xmax, xcenter, ymin, ymax, ycenter)

			# specify the coordinate system of our turtle screen
			screen.setworldcoordinates(xmin - 0.20 * xsize, 
									   ymin - 0.20 * ysize,
									   xmax + 0.20 * xsize,
									   ymax + 0.20 * ysize
									  )

			# draw the x-axis & y-axis line
			turtle_obj.ht()

			turtle_obj.penup()
			turtle_obj.goto(xmin, ymax)
			turtle_obj.pendown()
			turtle_obj.goto(xmin, ymin)
			turtle_obj.goto(xmax, ymin)
			turtle_obj.penup()


			# draw the x-axis & y-axis title label
			turtle_obj.goto(xcenter, ymin - 0.10 * ysize)
			turtle_obj.write(xlabel, align="center", font=("Arial", 12, "bold"))

			turtle_obj.goto( xmin - 0.10 * xsize, ycenter)
			turtle_obj.write(ylabel, align="center", font=("Arial", 12, "bold"))



			# draw the x-axis & y-axis numbering
			number_of_x_decimal_places = max( 4 - math.floor( math.log(xsize, 10) ),   0)
			number_of_y_decimal_places = max( 4 - math.floor( math.log(ysize, 10) ),   0)

			for i in range(0, 101, 10):


				## TODO: THE X-AXIS NUMBERING

				# every 10% of x-axis will be numbered
				x = xmin + (xsize * i / 100.0)				# i% of {xsize} + {xmin}


				# at {x} draw the numbering short line (vertical)
				turtle_obj.penup()
				turtle_obj.goto(x, ymin+0.025*ysize)
				turtle_obj.pendown()
				turtle_obj.goto(x, ymin-0.025*ysize)


				# at {x} draw the number
				turtle_obj.penup()
				turtle_obj.goto(x, ymin-0.05*ysize)
				turtle_obj.pendown()
				turtle_obj.write(f"{x:.{number_of_x_decimal_places}f}", align="right", font=("Arial", 9, "normal"))




				## TODO: THE Y-AXIS NUMBERING

				# every 10% of y-axis will be numbered
				y = ymin + (ysize * i / 100.0)				# i% of {ysize} + {ymin}


				# at {y} draw the numbering short line (horizontal)
				turtle_obj.penup()
				turtle_obj.goto(xmin+0.025*xsize, y)
				turtle_obj.pendown()
				turtle_obj.goto(xmin-0.025*xsize, y)


				# at {y} draw the number
				turtle_obj.penup()
				turtle_obj.goto(xmin-0.05*xsize, y)
				turtle_obj.pendown()
				turtle_obj.write(f"{y:.{number_of_y_decimal_places}f}", align="right", font=("Arial", 9, "normal"))



			# list of all sequence element in plot
			sequences = plot_element.getElementsByTagName("Sequence")

			# keep track of turtle object initial color
			turtle_obj_initial_color = turtle_obj.color()


			for i in range(len(sequences)):

				# obtain sequence attributes: title & color
				sequence_title = sequences[i].attributes["title"].value.strip()
				sequence_color = sequences[i].attributes["color"].value.strip()


				# position of the sequence title
				x_plot_label = xcenter
				y_plot_label = ymax - ((0.10 * i) * ysize) 


				# write sequence title
				turtle_obj.color(sequence_color)
				turtle_obj.penup()
				turtle_obj.goto(xcenter, y_plot_label)
				turtle_obj.write(sequence_title, align="center", font=("Arial" ,14 , "bold"))


				# obtain each datapoint location & place a "dot" at location
				sequence_datapoints = sequences[i].getElementsByTagName("DataPoint")
				for datapoint in sequence_datapoints:

					datapoint_x = float(datapoint.attributes["x"].value.strip())
					datapoint_y = float(datapoint.attributes["y"].value.strip())

					turtle_obj.goto(datapoint_x, datapoint_y)

					turtle_obj.dot()


			# update the turtle screen(showing the plot)
			screen.update()


		# call the buildWindow main function
		buildWindow_main()




if __name__ == "__main__":
	main()





			

# BETTER STYLISTIC ADDITIONS
# write a function that returns a particular percent of a number 
# e.g 10% of 10 = 1 

# deal with all your assumption about the plot file 
# by building contigencies in case its not how it should be
# for instance what if a particular plot file has no plot element
# make sure you code does not break in this circumstances


