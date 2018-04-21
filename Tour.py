# This class encodes our routes, referred to as tours

from random import shuffle

class Tour:

	# Construct a blank tour if not specified
	def __init__(self, tm, tour=None):
		self.tm = tm
		# Holds tour of cities
		self.__tour = []

		# Cache
		self.__fitness = 0
		self.__distance = 0

		if tour == None:
			for i in range(self.tm.number_of_cities()):
				self.__tour.append(None)
		else:
			self.__tour = tour

	# Creates a random individual
	def generate_individual(self):
		for city_index in range(self.tm.number_of_cities()):
			self.set_city(city_index, self.tm.get_city(city_index))
		shuffle(self.__tour)

	# Get city from tour
	def get_city(self, tour_position):
		return self.__tour[tour_position]

	# Set city in certain position within a tour
	def set_city(self, tour_position, city):
		self.__tour[tour_position] = city
		self.__fitness = 0
		self.__distance = 0

	# Get tours fitness
	def get_fitness(self):
		if self.__fitness == 0:
			self.__fitness = 1/self.get_distance()
		
		return self.__fitness

	# Get total distance of tour
	def get_distance(self):
		if self.__distance == 0:
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
		return len(self.__tour)

	# Check if tour contains a specific city
	def contains_city(self, city):
		return city in self.__tour

	def to_string(self):
		gene_string = ''
		gene_string = '(' + self.get_city(0).to_string() + ')'
		for i in range(1, self.tour_size()):
			gene_string +=  '->' + str(self.get_city(i).distance_to(self.get_city(i-1))) + '->' + '(' + self.get_city(i).to_string() + ')'
		#return gene_string
		return str(self.get_city(2).distance_to(self.get_city(1)))

