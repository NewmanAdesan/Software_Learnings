

PROGRAM LAYOUT:
```````````````
Basically this project is divided into FIVE SECTIONS
	1. SET UP DRAWING AREA (CANVAS)

	2. SET UP TOOLS AREA 

	3. SET UP TOOLS CALLBACKS (BUTTON FUNCTIONALITY)

	4. SET UP CANVAS EVENT HANDLERS

	5. SET UP MENU OPTIONS




* SET UP DRAWING AREA (CANVAS):
	- set up a tkinter root window named "root"

	- "root" houses a tkinter canvas widget named "canvas"

	- set up a raw turtle object named "pen" which draws on "canvas"




* SET UP TOOLS AREA:

	PRE-REQUISITE:
		- Firstly, Lets know the basic tools in our drawing application
			Command to draw Circle
			Command to begin fill
			Command to end fill
			Command to pen up
			Command to pen down

		- We instruct the turtle object to carry out this command on it's canvas

		- let's visit the ingredient for each command.
		  because both the ingredient and the command itself will influence
		  the set of tools in our TOOLS AREA.


		- Command to draw Circle(3):
			"radius" -  circle radius
			"width"  -  width of the pen
			"color"  -  color of the pen


		- Command to begin fill(1):
			"color" - fill color


		- Command to end fill / pen up / pen down :
			no ingredient needed

		- This knowledge tells us the basic tools of our drawing application
			- "radius" text box
			- "width" text box
			- "pen color" text box
			- "fill color" text box

			{You can deal with user entry error if you want}

			- draw circle button
			- begin fill button
			- end fill button
			- pen up button
			- pen down button


	TODO:
		- set up a tkinter frame widget named "side bar" 
		  packed at the left side of "root"

		- add the textbox widgets and button widgets to the "side bar"




* SET UP BUTTON FUNCTIONALITY:

	PRE-REQUISITE:
		- Because we aim to store commands in a file (xml format)
		  after drawing is done,

		- we would encapsulate each command as a Class
			"CircleCommand class"
			"BeginFillCommand class"
			"EndFillCommand class"
			"PenUpCommand class"
			"PenDownCommand class"

		- we use classes, so we can have a container (list)
		  that store commands (command object)

		- from a particular container, we can run through its command object
		  and create an xml file format, storing the drawing.

		- every command object has 2 basic tasks
			+ To draw
				instruct turtle to draw command on turtle "draw method"

			+ To show
				obtain xml element denoting command "__str__ method"

				By returning a string like this from each of the command objects, 
				the code to write the draw program’s data to a file is very simple.


		- for example, xml format for a Circle Command
		  <Command radius="20.0" width="1" color="black">Circle</Command>


	TODO:
		- For each Command button, the functionality follows this pattern
			+ create a class object for command
			+ draw the command via object class method
			+ add the command object to program's container(list)




* SET UP CANVAS EVENT HANDLERS:
	- Basically we have (3) event handlers
		+ mouse click event 
		+ mouse drag event
		+ "u" key press event (undo)

	- the mouse click & mouse drag event controls 
	  the position of the turtle object "pen" on the canvas

	- to control "pen" position brings us to one last command
	  the "GoToCommand class"

	- Command to move turtle object to (x,y)
	  whose ingredients are:
		+ x coord
		+ y coord
		+ width   - width of "pen"
		+ color   - color of "pen"


	- the undo handler implemented by the "u" key
	  simply 'undo the last draw step'
	  	+ remove the last draw command from the container(list)
	  	+ reset the turtle object by:
	  		clearing it's drawing
	  		going to initial position
	  	+ redraws each command object in the container on the canvas 





* SET UP MENU OPTIONS:
	- Basically there are (5) file menu options
		+ New
		+ Load...
		+ Load Into...
		+ Save As...
		+ Exit

	- New option
		This pretty much creates a new canvas.
		clearing turtle drawing, 
		setting turtle to initial state,
		clearing programs draw command objects container(graphics command list).
		{
			prompt a askyesnocancel message box
			in the case there are content in graphics command list
		}


	- Load...
		This collects an XML file depicting drawing commands
		converts all the drawing command in the xml file into it respective Command class
		places the Command objects in the program container(graphics command list)
		over-riding what was in the container(list)
		draws each command


	- Load Into..
		This is similar to the Load menu functionality
		But it does not Override the program's draw command container
		Instead, it adds to the container
		So user can add external drawing to current drawing

		To append two graphics command list together
		we need to add some commands in-between, 
		so that turtle state of the current graphics command 
		don't affect the external graphics command

		Think about it,
		if we were to draw the file graphics commands on it owns, like the "load_option"
		it will assume the turtle is at "goto(0, 0)" and the pen is down

		We have to make sure this assumptions still hold
		that is why, in-between we will implicitly 
		add GoToCommand and PenDown Command to the graphics command list.
		also we reset the turtle on the canvas


	- Save As...
		This convert the graphics command list into an XML file
		by writing each command object in the graphics command list into a file 
		whose filename is specified by user.


	- Exit
		exits the drawing application





EXTRA NOTE:
```````````
Notice
	- the entries to the text box widget in "side bar",
	- does not affect when the program itself is drawing
	- cases where the program itself is drawing includes
		+ when the undo handler is invoked
		+ when the load menu option is chosen
		+ when the load_into.. menu option is chosen
	- it only affects when the user draws, and this is a typical thinking
	- because they are only used when the button is pressed typically


Notice
	- the "pseudo-inefficiency" of connecting the GoTo commmand with mouse click drag. 
	- it depends solely on how the click drag is implemented
	- because for little mouse drag, 40 goto command can be added to the list.
	- thus for a large graphics, the append command will be used a lot


Notice
	- the problem of the procedural approach
	- when referencing the global binding,
	- if we are going to override the global binding in any method
	- like we do in the "New menu" & "Load... menu" functionality,
	- we need use the "global keyword" so we dont create a local binding






OOP APPROACH:
`````````````
	- This still follows the procedural approach 
	- the difference is that the five stages of the drawing application 
	- is encapsulated in a class called "DrawingApplication"
	- which will be a "sub-class" of the tkinter frame widget

	- we have a user-defined frame widget class "DrawingApplication"
	- such that, when it is instantiated,
		+ the drawing area (canvas)
		+ the tools area (side_bar)
		+ the button functionalities
		+ the canvas event handlers
		+ the menu options
	- will all be set up, functional and running


	- in the main.py file,
	- we create a tkinter window widget named "root"
	- we instatiante DrawingApplication class named "app"
	- place "app" which is also a frame widget inside "root"
	- the rest is history







EXTRA FEATURES:
```````````````
	1. ADD A NEW GRAPHICS COMMAND EASY
		- Starting with the version of the Draw program 
		- add a new graphics command of your choice to the program.

		- Consider how it would be written to a file, 
		- create a test file, write your code, and test it. 

		- You must design two files: a sample test file, and the program itself.

		- Some examples might be a graphics command 
			+ to draw a star with some number of points, 
			+ a rectangle with a height and width



	2. ADD A NEW GRAPHICS COMMAND EXTRA
		- Starting with the Draw program provided, 
		- extend the program to include a new button 
		- to draw a new shape for the Draw program. 

		- For instance, have the draw program draw 
		- a star on the screen or 
		- a smiley face or something of your choosing. 

		- HINT: If you use the forward and back methods to draw your shape, 
		- you can scale it by multiplying each forward and back amount by a scale value. 
		- Then, you can let the user pick a scale for it 
		  (or use the radius amount as your scale) and 
		  draw your shape in whatever size you like. 

		- To complete this exercise 
		- you must extend your XML format to include a new graphics command
		- to store the relevant information for drawing your new shape. 
		- You must also define a new graphicsCommand class for your new shape.



	3. ADD COMMAND TO DRAW A STRING ON CANVAS
		- Add the ability to draw a text string on a Draw picture. 
		- You’ll need to let the user pick a point size. 

		- For a real challenge, let the user pick the font type 
		- from a drop-down list of font types. 
		- Draw a string that you have the user enter in an entry box.



	4. GRAPH AN XML FILE
		- Find an XML document of your choice on the internet, 
	   	- write code to parse through the data and plot something 
	   	- from that data whether it be some value over time or something else. 
	   	- Use turtle graphics to plot the data that you find.



	5. ADD RAINBOW BUTTON
		- Add a new button to the drawing program 
		- that draws a rainbow centered above the current location of the turtle. 

		- This can be done quite easily by using sin and cos (i.e. sine and cosine). 
		- The sin and cos functions take radians as a parameter.

		- To draw a rainbow, 
		- the radians would range from 0 to math.pi from the math module. 

		- You must import the math module to get access 
		- to math.cos and math.sin as well as math.pi. 

		- To draw values in an arc, 
		- you can use a for loop and let a variable, i, range from 0 to 100. 
		- Then radius * math.cos(i/100.0 * math.pi), 
		- radius * math.sin(i/100.0 * math.pi) 
		- is the next x,y coordinate of the rainbow’s arc. 

		- By varying the radius you will get several stripes for your rainbow.







