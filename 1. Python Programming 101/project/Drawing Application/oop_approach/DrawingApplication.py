#!python3


import tkinter
import tkinter.colorchooser
import tkinter.filedialog

import turtle

import GraphicCommands
import xml.dom.minidom 

import sys
import os



class DrawingApplication(tkinter.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.graphics_command = GraphicCommands.PyList()
		self.build_window()
		self.pack()


	def build_window(self):
		

		#-------  TODO: SET UP DRAWING AREA  ---------#
		# add title to the root window (the window that houses, this frame class)
		self.master.title("Draw Program")

		#create the canvas widget
		canvas = tkinter.Canvas(self, width=600, height=600)
		canvas.pack(side=tkinter.LEFT)

		#create raw turtle with the canvas widget
		the_turtle = turtle.RawTurtle(canvas)
		the_turtle.shape("circle")

		# get the screen object of the turtle, set the screen object to update on demand
		screen = the_turtle.getscreen()
		screen.tracer(0)




		#------- TODO: SET UP TOOLS AREA (FRONT-END) ---------#
		# create the side bar frame
		side_bar = tkinter.Frame(self, padx=5, pady=5)
		side_bar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

		# place the width label
		width_label = tkinter.Label(side_bar, text="Width")
		width_label.pack()

		# place the width entry box
		width_size = tkinter.StringVar()
		width_entry = tkinter.Entry(side_bar, textvariable=width_size)
		width_entry.pack()
		width_size.set("1")

		# place the radius label
		radius_label = tkinter.Label(side_bar, text="Radius")
		radius_label.pack()

		# place the radius entry box
		radius_size = tkinter.StringVar()
		radius_entry = tkinter.Entry(side_bar, textvariable=radius_size)
		radius_entry.pack()
		radius_size.set("10")

		# place the Draw Circle button
		circle_button = tkinter.Button(side_bar, text="Draw Circle")
		circle_button.pack(fill=tkinter.BOTH)


		# place the pen color and fill color buttons, label and entry
		screen.colormode(255)

		pencolor_label = tkinter.Label(side_bar, text="Pen Color")
		pencolor_label.pack()

		pencolor = tkinter.StringVar()
		pencolor_entry = tkinter.Entry(side_bar, textvariable=pencolor)
		pencolor_entry.pack()
		pencolor.set("#000000")

		pencolor_button = tkinter.Button(side_bar, text="Pick Pen Color")
		pencolor_button.pack(fill=tkinter.BOTH)

		fillcolor_label = tkinter.Label(side_bar, text="Fill Color")
		fillcolor_label.pack()

		fillcolor = tkinter.StringVar()
		fillcolor_entry = tkinter.Entry(side_bar, textvariable=fillcolor)
		fillcolor_entry.pack()
		fillcolor.set("#000000")

		fillcolor_button = tkinter.Button(side_bar, text="Pick Fill Color")
		fillcolor_button.pack(fill=tkinter.BOTH)

		# place the begin fill button
		beginfill_button = tkinter.Button(side_bar, text="Begin Fill")
		beginfill_button.pack(fill=tkinter.BOTH)

		# place the end fill button
		endfill_button = tkinter.Button(side_bar, text="End Fill")
		endfill_button.pack(fill=tkinter.BOTH)

		# place the pen up and pen down button and a feedback label
		pen_label = tkinter.Label(side_bar, text="Pen is Down")
		pen_label.pack()

		penup_button = tkinter.Button(side_bar, text="Pen Up")
		penup_button.pack(fill=tkinter.BOTH)

		pendown_button = tkinter.Button(side_bar, text="Pen Down")
		pendown_button.pack(fill=tkinter.BOTH)



		#------- TODO: SET UP TOOLS CALLBACKS (BACK-END) ---------#
		# Define draw circle callback
		def circle_callback():
			# create a circle command structure
			cmd = GraphicCommands.CircleCommand(float(radius_size.get()), float(width_size.get()), pencolor.get())
			cmd.draw(the_turtle)
			self.graphics_command.append(cmd)

			# update canvas to show drawing, set event focus on canvas
			screen.update()
			screen.listen()	


		circle_button.configure(command=circle_callback)


		# Define pick pen color and pick fill color callback
		def set_color(var):
			# ask for a color via tkinter colorchooser
			color = tkinter.colorchooser.askcolor()

			# set the set tkinter StringVar variable to choosen color
			if color != None:
				var.set(str(color)[-9:-2])

		pencolor_button.configure(command= lambda x=pencolor: set_color(x))
		fillcolor_button.configure(command= lambda x=fillcolor: set_color(x))


		# Define Begin Fill callback
		def beginfill_callback():
			# create a begin fill command structure
			cmd = GraphicCommands.BeginFillCommand(fillcolor.get())
			cmd.draw(the_turtle)
			self.graphics_command.append(cmd)


		beginfill_button.configure(command=beginfill_callback)


		# Define End Fill callback
		def endfill_callback():
			# create a begin fill command structure
			cmd = GraphicCommands.EndFillCommand()
			cmd.draw(the_turtle)
			self.graphics_command.append(cmd)


		endfill_button.configure(command=endfill_callback)


		# Define Pen Up callback
		def penup_callback():
			cmd = GraphicCommands.PenUpCommand()
			cmd.draw(the_turtle)
			self.graphics_command.append(cmd)

			pen_label.configure(text="Pen is Up")

		penup_button.configure(command=penup_callback)



		# Define Pen Down callback
		def pendown_callback():
			cmd = GraphicCommands.PenDownCommand()
			cmd.draw(the_turtle)
			self.graphics_command.append(cmd)

			pen_label.configure(text="Pen is Down")

		pendown_button.configure(command=pendown_callback)





		#------- TODO: SET UP CANVAS EVENT HANDLERS  ---------#
		# Event handling when the canvas is clicked
		def click_handler(x, y):
			cmd = GraphicCommands.GoToCommand(x, y, float(width_size.get()), pencolor.get())
			cmd.draw(the_turtle)
			self.graphics_command.append(cmd)

			screen.update()
			screen.listen()

		screen.onclick(click_handler)


		# Event handling when the mouse is dragged on the canvas
		def drag_handler(x, y):
			click_handler(x, y)

		the_turtle.ondrag(drag_handler)



		# Event handling to "UNDO" the last command
		# this is done by removing the last command from list and redrawing the entire picture
		def undo_handler():
			self.graphics_command.remove_last()
			the_turtle.clear()
			the_turtle.penup()
			the_turtle.goto(0, 0)
			the_turtle.pendown()

			for cmd in self.graphics_command:
				cmd.draw(the_turtle)

			screen.update()
			screen.listen()

		screen.onkeypress(undo_handler, "u") 
		screen.listen()






		#------- TODO: SETTING UP MENU OPTIONS  ---------#

		# Setup inner and outer layer menu widget object to root window (self.master)
		outer_menu = tkinter.Menu()
		self.master.configure(menu=outer_menu)

		inner_menu = tkinter.Menu(outer_menu, tearoff=0)

		# ADD "New" Option and its functionality
		def new_option():
			the_turtle.clear()
			the_turtle.penup()
			the_turtle.goto(0, 0)
			the_turtle.pendown()
			self.graphics_command = GraphicCommands.PyList()

			screen.update()
			screen.listen()

		inner_menu.add_command(label="New", command=new_option)



		# ADD "Load.." Option and its functionality
		def load_option():

			# create a new canvas
			new_option()

			# prompt user to choose a file via "tkinter file dialog"
			filename = tkinter.filedialog.askopenfilename(initialdir='.', filetypes=[('Text files', '.txt'), ('All files', '*')])

			# parse the xml file into a list of graphics command
			self.graphics_command = self.parse(filename)

			# draw the commands in the loaded file
			for command in self.graphics_command:
				command.draw(the_turtle)

			screen.update()
			screen.listen()


		inner_menu.add_command(label="Load...", command=load_option)



		# ADD "Load Into..." Option and its functionality
		def load_into_option():

			# prompt user to choose a file via "tkinter file dialog"
			filename = tkinter.filedialog.askopenfilename(initialdir='.', filetypes=[('Text files', '.txt'), ('All files', '*')])
		
			# parse the xml file into a graphics command list
			external_graphics_command = self.parse(filename)

			# To append two graphics command list together
			# we need to add some commands in-between, 
			# so that turtle state of the current graphics command don't affect the parsed file graphics command

			# Think about it,
			# if we were to draw the file graphics commands on it owns, like the "load_option"
			# it will assume the turtle is at "goto(0, 0)" and the pen is down

			# We have to make sure this assumptions still hold
			# that is why, in-between we will implicitly add GoToCommand and PenDown Command
			# to the graphics command list.
			# also we set the turtle to "goto(0, 0)"

			# LET'S GET TO IT

			cmd = GraphicCommands.PenUpCommand()
			the_turtle.penup()
			self.graphics_command.append(cmd)

			cmd = GraphicCommands.GoToCommand(0.0, 0.0, 1.0, "#000000")
			the_turtle.goto(0, 0)
			self.graphics_command.append(cmd)

			cmd = GraphicCommands.PenDownCommand()
			the_turtle.pendown()
			self.graphics_command.append(cmd)

			for command in external_graphics_command:
				self.graphics_command.append(command)

			for command in self.graphics_command:
				command.draw(the_turtle)

			screen.update()
			screen.listen()


		inner_menu.add_command(label="Load Into...", command=load_into_option)



		# ADD "Save As..." Option and its functionality
		def save_as_option():
			filename = tkinter.filedialog.asksaveasfilename(initialdir='.', filetypes=[('Text files', '.txt'), ('All files', '*')])

			if not os.path.basename(filename).endswith(".txt"):
				filename += ".txt"

			with open(filename, "w") as file:

				# line to identify xml file
				file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n\n')

				# write parent command opening tag
				file.write('<GraphicsCommands>\n')

				# write each command in graphics command list
				for command in self.graphics_command:
					file.write('\t'+ str(command) +'\n')

				# write parent command closing tag
				file.write('</GraphicsCommands>\n')


		inner_menu.add_command(label="Save As...", command=save_as_option)




		# ADD "Exit" Option and its functionality
		def exit_option():
			sys.exit(1)
			
		inner_menu.add_command(label="Exit", command=exit_option)

		outer_menu.add_cascade(label="File", menu=inner_menu)



	def parse(self, filename):

		commands_list = GraphicCommands.PyList()

		# xml.dom.minidom.Document object for the file
		xml_doc = xml.dom.minidom.parse(filename)

		# First Dom Element object for "GraphicsCommands" tag
		gc_element = xml_doc.getElementsByTagName("GraphicsCommands")[0]

		# list of Dom Element object for "Command" tag
		command_elements = gc_element.getElementsByTagName("Command")

		# for each command, create a Command Structure, add to the graphics command list
		for command_element in command_elements:
			name = command_element.firstChild.data.strip()
			attr = command_element.attributes

			# create an if/else tree to handle each type of command
			if name == "GoTo":
				x = float(attr['x'].value)
				y = float(attr['y'].value)
				width = float(attr['width'].value)
				color = attr["color"].value.strip()

				cmd = GraphicCommands.GoToCommand(x, y, width, color)

			elif name == "Circle":
				radius = float(attr["radius"].value)
				width = float(attr["width"].value)
				color = attr["color"].value.strip()

				cmd = GraphicCommands.CircleCommand(radius, width, color)

			elif name == "BeginFill":
				color = attr["color"].value.strip()
				cmd = GraphicCommands.BeginFillCommand(color) 


			elif name == "EndFill":
				cmd = GraphicCommands.EndFillCommand() 


			elif name == "PenUp":
				cmd = GraphicCommands.PenUpCommand() 


			elif name == "PenDown":
				cmd = GraphicCommands.PenDownCommand()


			commands_list.append(cmd)

		return commands_list




def main():
	root = tkinter.Tk();
	drawing_app = DrawingApplication(root)

	drawing_app.mainloop()
	print("Program Execution Completed")


if __name__ == '__main__':
	main()
