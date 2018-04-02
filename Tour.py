# This class encodes our routes, referred to as tours

import Tour_Manager
from random import shuffle

class Tour:

	# Construct a blank tour if not specified
	def __init__(self, tour=None):
		# Cache
		self.fitness = 0
		self.distance = 0

		if tour is None:
			self.tour = []
			for i in range(Tour_Manager.number_of_cities()):
				self.tour.append(None)
		else:
			self.tour = tour

	# Creates a random individual
	def generate_individual(self):
		for city_index in range(Tour_Manager.number_of_cities()):
			self.set_city(city_index, Tour_Manager.get_city(city_index))
		shuffle(self.tour)

	# Get city from tour
	def get_city(self, tour_position):
		return self.tour[tour_position]

	# Set city in certain position within a tour
	def set_city(self, tour_position, city):
		self.tour[tour_position] = city
		self.fitness = 0
		self.distance = 0

	# Get tours fitness
	def get_fitness(self):
		if self.fitness == 0:
			self.fitness = 1/self.get_distance()
		
		return self.fitness

	# Get total distance of tour
	def get_distance(self):
		if distance == 0:
			tour_distance = 0
			for city_index in range(self.tour_size()):
				
				# City we're travelling from
				from_city = self.get_city(city_index)

				# City we're travelling to
				if (city_index+1 < self.tour_size()):
					destination_city = self.get_city(city_index+1)
				else:
					destination_city = self.get_city(0)

				# Get distance b/t two cities
				tour_distance += from_city.distance_to(destination_city)

			distance = tour_distance

		return distance

	# Get number of cities in our tour
	def tour_size(self):
		return len(self.tour)

	# Check if tour contains a specific city
	def contains_city(self, city):
		return city in self.tour

	def to_string(self):
		gene_string = ''
		for i in range(self.tour_size()):
			gene_string += self.get_city(i) + '|'
		return gene_string


