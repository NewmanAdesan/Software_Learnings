#!python3 
"""
	With experimentation 
		- we can verify that all locations 
		- within the RAM of a computer
		- can be accessed in the same amount of time.
		- despite the size 
"""


import sys
import random

import time
import datetime

with open("data.xml", "w") as file:
	file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
	file.write('<Plot title="Average List Element Access Time">\n')


	## TODO: First plot - Average Access Time vs List Size
	## program test average access time for different list size

	# range of list size
	x_min = 1000
	x_max = 200000
	step = 1000

	
	# list structure to store data
	x_data = []
	y_data = []

	for size in range(x_min, x_max+1, step):

		# add x data-point
		x_data.append(size)

		# we will perform a minor computation when we access the value
		product = 0

		# obtain zero-filled list of current size
		lst = [0] * size

		# let the garbage collection/memory allocation settle down
		time.sleep(1)

		# perform a timed 1000 access on the list per size
		# obtain the average access time
		start_time = time.time()

		for i in range(1000):

			# obtain a random location & its value
			loc = random.randint(0, size-1)
			val = lst[loc]

			# dummy operation with value, to ensure it is retrieved
			product *= val

		end_time = time.time()


		# average time in seconds for access 
		t = (end_time - start_time) / 1000
		# deltaT = end_time - start_time
		# accessTime = deltaT.total_seconds() * 1000


		# conversion to milliseconds
		t = round(t * 1000000, 3)

		# add y data-point
		y_data.append(t)


	# Axes information
	file.write('\t' + '<Axes>' + '\n')
	file.write('\t\t' + f'<XAxis min="{x_min}" max="{x_max}">List Size</XAxis>' + '\n')
	file.write('\t\t' + f'<YAxis min="{min(y_data)}" max="{max(y_data)}">Microseconds</YAxis>' + '\n')
	file.write('\t' + '</Axes>' + '\n')

	# Add datapoints
	file.write('\t' + '<Sequence title="Average Access Time vs List Size" color="red">\n')
	for i in range(len(x_data)):
		file.write('\t\t' + f'<DataPoint x="{x_data[i]}" y="{y_data[i]}"/>\n')
	file.write('\t' + '</Sequence>\n')
	file.write('</Plot>\n')








	
			
