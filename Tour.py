# This class encodes our routes, referred to as tours

import Tour_Manager
from random import shuffle

class Tour:

	# Holds tour of cities
	__tour = []

	# Cache
	__fitness = 0
	__distance = 0

	# Construct a blank tour if not specified
	def __init__(self, tour=None):

		if tour == None:
			for i in range(Tour_Manager.number_of_cities()):
				__tour.append(None)
		else:
			__tour = tour

	# Creates a random individual
	def generate_individual(self):
		for city_index in range(Tour_Manager.number_of_cities()):
			self.set_city(city_index, Tour_Manager.get_city(city_index))
		shuffle(__tour)

	# Get city from tour
	def get_city(self, tour_position):
		return __tour[tour_position]

	# Set city in certain position within a tour
	def set_city(self, tour_position, city):
		__tour[tour_position] = city
		__fitness = 0
		__distance = 0

	# Get tours fitness
	def get_fitness(self):
		if __fitness == 0:
			__fitness = 1/self.get_distance()
		
		return __fitness

	# Get total distance of tour
	def get_distance(self):
		if distance == 0:
			tour_distance = 0
			for city_index in range(__tour_size()):
				
				# City we're travelling from
				from_city = self.get_city(city_index)

				# City we're travelling to
				if (city_index+1 < __tour_size()):
					destination_city = self.get_city(city_index+1)
				else:
					destination_city = self.get_city(0)

				# Get distance b/t two cities
				tour_distance += from_city.distance_to(destination_city)

			distance = tour_distance

		return distance

	# Get number of cities in our tour
	def tour_size(self):
		return len(__tour)

	# Check if tour contains a specific city
	def contains_city(self, city):
		return city in __tour

	def to_string(self):
		gene_string = ''
		for i in range(__tour_size()):
			gene_string += self.get_city(i) + '|'
		return gene_string


