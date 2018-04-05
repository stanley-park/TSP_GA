# This is the main class that creates a tour of cities and evolves the solution
import City
import Tour_Manager as tm
import Tour
import Population
import Genetic_Algorithm

def main():

	# Create and add our cities
	city1 = City.City(60, 200)
	print(type(city1))
	tm.add_city(city1)
	city2 = City.City(180, 200)
	tm.add_city(city2)
	city3 = City.City(80, 180)
	tm.add_city(city3)
	city4 = City.City(140, 180)
	tm.add_city(city4)
	city5 = City.City(20, 160)
	tm.add_city(city5)
	city6 = City.City(100, 160)
	tm.add_city(city6)
	city7 = City.City(200, 160)
	tm.add_city(city7)
	city8 = City.City(140, 140)
	tm.add_city(city8)
	city9 = City.City(40, 120)
	tm.add_city(city9)
	city10 = City.City(100, 120)
	tm.add_city(city10)
	city11 = City.City(180, 100)
	tm.add_city(city11)
	city12 = City.City(60, 80)
	tm.add_city(city12)
	city13 = City.City(120, 80)
	tm.add_city(city13)
	city14 = City.City(180, 60)
	tm.add_city(city14)
	city15 = City.City(20, 40)
	tm.add_city(city15)
	city16 = City.City(100, 40)
	tm.add_city(city16)
	city17 = City.City(200, 40)
	tm.add_city(city17)
	city18 = City.City(20, 20)
	tm.add_city(city18)
	city19 = City.City(60, 20)
	tm.add_city(city19)
	city20 = City.City(160, 20)
	tm.add_city(city20)

	# Initialize population
	pop = Population(50, True)
	print("Initial Distance: " + str(pop.get_fittest().get_distance()))

	# Evolve population for 100 generations
	for i in range(101):
		pop = Genetic_Algorithm.evolve_population(pop)

	# Print results
	print("Finished")
	print("Final Distance: " + str(pop.get_fittest().get_distance()))
	print("Solution: ")
	print(str(pop.get_fittest()))

if __name__ == "__main__":
	main()



	