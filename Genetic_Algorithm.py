# Genetic_Algorithm.py manages algorithm for evolving population

import Population

class Genetic_Algorithm:

	def __init__(self):

		self.mutation_rate = 0.015
		self.tournament_size = 5
		self.elitism = True

	# Evolves a population over one generation
	def evolve_population(self, pop):
		new_population = Population(pop.population_size(), false)

		# Keep our best individual if elitism is enabled
		elitism_offset = 0
		if self.elitism:
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
	


















