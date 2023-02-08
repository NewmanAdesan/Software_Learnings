#!python3


import turtle

class GoToCommand:
	def __init__(self, x, y, width, color):
		self.x = x
		self.y = y
		self.width = width
		self.color = color

	def draw(self, turtle):
		turtle.width(self.width)
		turtle.pencolor(self.color)
		turtle.goto(self.x, self.y)


	def __str__(self):
		return f'<Command x="{self.x}" y="{self.y}" width="{self.width}" color="{self.color}">GoTo</Command>'



class CircleCommand:
	def __init__(self, radius, width, color):
		self.radius = radius
		self.width = width
		self.color = color

	def draw(self, turtle):
		turtle.width(self.width)
		turtle.pencolor(self.color)
		turtle.circle(self.radius)


	def __str__(self):
		return f'<Command radius="{self.radius}" width="{self.width}" color="{self.color}">Circle</Command>'
		


class BeginFillCommand:
	def __init__(self, color):
		self.color = color

	def draw(self, turtle):
		turtle.fillcolor(self.color)
		turtle.begin_fill()


	def __str__(self):
		return f'<Command color="{self.color}">BeginFill</Command>'



class EndFillCommand:
	def __init__(self):
		pass

	def draw(self, turtle):
		turtle.end_fill()


	def __str__(self):
		return f'<Command>EndFill</Command>'



class PenUpCommand:
	def __init__(self):
		pass

	def draw(self, turtle):
		turtle.penup()


	def __str__(self):
		return f'<Command>PenUp</Command>'



class PenDownCommand:
	def __init__(self):
		pass

	def draw(self, turtle):
		turtle.pendown()


	def __str__(self):
		return f'<Command>PenDown</Command>'

		


class PyList:
	def __init__(self):
		self.list = []

	def append(self, item):
		self.list.append(item)

	def remove_last(self):
		if len(self.list)>0:
			self.list.pop()

	def __iter__(self):
		"""
			if we want to iterate over this sequence, 
			we define the special method called __iter__(self). 

			Without this we’ll get "builtins.TypeError:

			’PyList’ object is not iterable" if we try to write 
			for cmd in seq:
			where seq is one of these sequences. 

			The yield below will yield an element of the sequence 
			and will suspend the execution of the for loop in the method below 
			until the next element is needed. 

			The ability to yield each element of the sequence 
			as needed is called "lazy" evaluation and is very powerful. 

			It means that we only need to provide access 
			to as many of elements of the sequence as are necessary and no more.
		"""
		for v in self.list:
			yield v


def main():

	# create our list data structure
	command_list = PyList()

	# define turtle object and turtle screen object
	t = turtle.Turtle()
	screen = t.getscreen()

	# obtain filename
	filename = r"C:\Users\hp\Music\Newman\Books\Data Structures and Algorithms with Python\1. Python Programming 101\truck.txt"

	# open the file object
	file = open(filename, "r")

	# loop through records in the file (loop and half pattern)
	command = file.readline().strip()

	while command != "":
		# parse each record into a Command structure
		# add the Command structure into Pylist object
		if command == "goto":
			x = float(file.readline())
			y = float(file.readline())
			width = float(file.readline())
			color = file.readline().strip()
			command_struct = GoToCommand(x, y, width, color)


		elif command == "circle":
			radius = float(file.readline())
			width = float(file.readline())
			color = file.readline().strip()
			command_struct = CircleCommand(radius, width, color)


		elif command == "beginfill":
			color = file.readline().strip()
			command_struct = BeginFillCommand(color)


		elif command == "endfill":
			command_struct = EndFillCommand()


		elif command == "penup":
			command_struct = PenUpCommand()


		elif command == "pendown":
			command_struct = PenDownCommand()

		else:
			raise RuntimeError("Unknown Command: " + command)


		command_list.append(command_struct)
		command = file.readline().strip()



	for cmd in command_list:
		cmd.draw(t)


	# close file
	file.close()

	# hide turtle
	t.ht()

	# exit window on click
	screen.exitonclick()

	print("Program execution completed")


if __name__ == '__main__':
	main()
