# This is the main class that creates a tour of cities and evolves the solution
import City
import Tour_Manager
import Tour
import Population
import Genetic_Algorithm
import numpy as np
import matplotlib.pyplot as plt
import ast

def main():
	tm = Tour_Manager.Tour_Manager()
	ga = Genetic_Algorithm.Genetic_Algorithm(tm)
	debug = False
	if debug:
		num_cities = int(input("How many cities do you want to add: "))
		list_of_coords = []
		for i in range(num_cities):
			city = input("Enter coordinate x and y separated by a comma: ")
			while city[0] == "(" or city[-1] == ")":
				if ',' not in city:
					city = input("Enter only x and y, and don't forget the comma between the coordinates: ")
				else:
					city = input("Try again, just enter x, y (e.g. 10,20; 30, 40; but not (40, 50) ")
			city = city.split(',')
			list_of_coords.append((int(city[0]), int(city[1])))
			city = City.City(int(city[0]), int(city[1]))
			tm.add_city(city)

	else:
		list_of_coords = [(60, 200), (180, 200), (80, 180), (140, 180), (20, 160), (100, 160), (200, 160),
		 					(140, 140), (40, 120), (100, 120), (180, 100), (60, 80), (120, 80), (180, 60),
		 					(20, 40), (100, 40), (200, 40), (20, 20), (60, 20), (160, 20)]
		print(list_of_coords)
		# Create and add our cities
		city1 = City.City(list_of_coords[0][0], list_of_coords[0][1])
		tm.add_city(city1)
		city2 = City.City(list_of_coords[1][0], list_of_coords[1][1])
		tm.add_city(city2)
		city3 = City.City(list_of_coords[2][0], list_of_coords[2][1])
		tm.add_city(city3)
		city4 = City.City(list_of_coords[3][0], list_of_coords[3][1])
		tm.add_city(city4)
		city5 = City.City(list_of_coords[4][0], list_of_coords[4][1])
		tm.add_city(city5)
		city6 = City.City(list_of_coords[5][0], list_of_coords[5][1])
		tm.add_city(city6)
		city7 = City.City(list_of_coords[6][0], list_of_coords[6][1])
		tm.add_city(city7)
		city8 = City.City(list_of_coords[7][0], list_of_coords[7][1])
		tm.add_city(city8)
		city9 = City.City(list_of_coords[8][0], list_of_coords[8][1])
		tm.add_city(city9)
		city10 = City.City(list_of_coords[9][0], list_of_coords[9][1])
		tm.add_city(city10)
		city11 = City.City(list_of_coords[10][0], list_of_coords[10][1])
		tm.add_city(city11)
		city12 = City.City(list_of_coords[11][0], list_of_coords[11][1])
		tm.add_city(city12)
		city13 = City.City(list_of_coords[12][0], list_of_coords[12][1])
		tm.add_city(city13)
		city14 = City.City(list_of_coords[13][0], list_of_coords[13][1])
		tm.add_city(city14)
		city15 = City.City(list_of_coords[14][0], list_of_coords[14][1])
		tm.add_city(city15)
		city16 = City.City(list_of_coords[15][0], list_of_coords[15][1])
		tm.add_city(city16)
		city17 = City.City(list_of_coords[16][0], list_of_coords[16][1])
		tm.add_city(city17)
		city18 = City.City(list_of_coords[17][0], list_of_coords[17][1])
		tm.add_city(city18)
		city19 = City.City(list_of_coords[18][0], list_of_coords[18][1])
		tm.add_city(city19)
		city20 = City.City(list_of_coords[19][0], list_of_coords[19][1])
		tm.add_city(city20)


	# Initialize population
	pop = Population.Population(50, True, tm)
	print("Initial Distance: " + str(pop.get_fittest().get_distance()))

	plt.title('Initial order of cities added')
	x, y = zip(*list_of_coords)
	plt.plot(x, y, 'xb-')
	plt.plot(x[0], y[0], 'go', label='Start')
	plt.plot(x[-1], y[-1], 'ro', label='End')
	plt.legend()
	plt.grid()
	plt.show()

	# Evolve population for 100 generations
	print("Evolving...")
	for i in range(251):
		pop = ga.evolve_population(pop)

	# Print results
	print("\nFinished\n")
	print("Final Distance: " + str(pop.get_fittest().get_distance()))
	print("Solution: ")
	print(pop.get_fittest().to_string())
	solution_path_coords = pop.get_fittest().to_string().split('->')
	for i in range(len(solution_path_coords)):
		if solution_path_coords[i] != '':
			solution_path_coords[i] = ast.literal_eval(solution_path_coords[i])
		else:
			del solution_path_coords[i]

	plt.title('Cities with path of shortest route')
	x, y = zip(*list_of_coords)
	plt.scatter(*zip(*list_of_coords))
	x_new, y_new = zip(*solution_path_coords)
	plt.plot(x_new, y_new, 'xb-')
	plt.plot(x_new[0], y_new[0], 'go', label='Start')
	plt.plot(x_new[-1], y_new[-1], 'ro', label='End')
	plt.legend()
	plt.grid()
	plt.show()

if __name__ == "__main__":
	main()



	