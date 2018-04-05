# Genetic_Algorithm.py manages algorithm for evolving population

import Population
import random

class Genetic_Algorithm:

	__mutation_rate = 0.015
	__tournament_size = 5
	__elitism = True

	# Evolves a population over one generation
	def evolve_population(self, pop):
		new_population = Population(pop.population_size(), false)

		# Keep our best individual if elitism is enabled
		elitism_offset = 0
		if __elitism:
			new_population.save_tour(0, pop.get_fittest())
			elitism_offset = 1

		# Crossover population
		# Loop over new population's size and creates individuals from current population
		for i in range(elitism_offset, new_population.population_size()):
			# Select parents
			parent_1 = self.tournament_selection(pop)
			parent_2 = self.tournament_selection(pop)

			# Crossover parents
			child = self.crossover(parent_1, parent_2)

			# Add child to new population
			new_population.save_tour(i, child)

		# Mutate the new population a bit to add some new genetic material
		for i in range(elitism_offset, new_population.population_size()):
			self.mutate(new_population.get_tour(i))

		return new_population

	# Applies crossover to a set of parents and creates offspring
	def crossover(self, parent_1, parent_2):
		
		# Create new child tour
		child = Tour()

		# Get start and end sub tour positions for p1's tour
		start_pos = int(random.random() * parent_1.tour_size())
		end_pos = int(random.random() * parent_1.tour_size())

		# Loop and add the sub tour from p1 to child
		for i in range(child.tour_size()):
			if start_pos < end_pos:
				child.set_city(i, parent_1.get_city())
			elif start_pos > end_pos:
				if (not (i < start_pos and i > end_pos)):
					child.set_city(i, parent_1.get_city())

		# Loop through p2 for remaining tours for child
		for i in range(parent_2.tour_size()):
			if (not(child.contains_city(parent_2.get_city()))):
				for j in range(child.tour_size()):
					if child.get_city(j) == None:
						child.set_city(j, parent_2.get_city(j))
						break

		return child

	# Mutate a tour using swap mutation
	def mutate(self, tour):

		for tour_pos_1 in range(tour.tour_size()):
			# Apply mutation rate
			if (random.random() < __mutation_rate):

				# Get second random position in the tour
				tour_pos_2 = int(tour.tour_size() * random.random())

				# Get cities at target position in tour
				city1 = tour.get_city(tour_pos_1)
				city2 = tour.get_city(tour_pos_2)

				# Swap them around
				tour.set_city(tour_pos_2, city1)
				tour.set_city(tour_pos_1, city2)

	# Selects candidate tour for crossover
	def tournament_selection(self, pop):

		tournament = Population(__tournament_size, False)

		# For each place in the tournament get a random candidate tour and add it
		for i in range(__tournament_size):
			random_id = int(random.random() * pop.population_size())
			tournament.save_tour(i, pop.get_tour(random_id))

		# Get fittest tour
		fittest = tournament.get_fittest()

		return fittest

















