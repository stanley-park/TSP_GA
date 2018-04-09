# This file manages a population of candidate tours

import Tour

class Population:

	def __init__(self, population_size, initialize, tm):
		self.tm = tm
		self.population_size = population_size
		self.tours = [None]*self.population_size
		if initialize:
			for i in range(population_size):
				new_tour = Tour.Tour(self.tm)
				new_tour.generate_individual()
				self.save_tour(i, new_tour)

	# Saves a tour to population
	def save_tour(self, index, tour):
		self.tours[index] = tour

	# Gets a tour
	def get_tour(self, index):
		return self.tours[index]

	# Gets the best tour in the population
	def get_fittest(self):
		fittest = self.tours[0]

		for i in range(self.population_size):
			if fittest.get_fitness() <= self.get_tour(i).get_fitness():
				fittest = self.get_tour(i)

		return fittest

	# Get population size
	def get_population_size(self):
		return len(self.tours)
