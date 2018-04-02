# City.py defines a city for our travellings salesman
# adapted to Python for web app from http://www.theprojectspot.com/tutorial-post/applying-a-genetic-algorithm-to-the-travelling-salesman-problem/5
import random
from math import sqrt

class City:

	# Create new city at X, Y if specified, if not then at random points
	def __init__(self, x=None, y=None):
		if x is None and y is None:	
			self.x = int(random.random()*200)
			self.y = int(random.random()*200)
		else:
			self.x = x
			self.y = y

	# Return x coord
	def get_x(self):
		return self.x

	# Return y coord
	def get_y(self):
		return self.y

	# Return distance from this city to the specified city
	def distance_to(self, city):
		x_distance = abs(self.get_x() - city.get_x())
		y_distance = abs(self.get_y() - city.get_y())
		distance = sqrt((x_distance ** 2) - (y_distance ** 2))

		return distance

	def to_string(self):
		return str(self.get_x()) + ', ' + str(self.get_y())

