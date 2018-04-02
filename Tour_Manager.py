# Tour Manager holds the destination cities of a tour in a TSP

class TourManager:

	def __init__(self):
		self.destination_cities = []

	# Add city to list of destinations on our tour
	def add_city(self, city):
		self.destination_cities.append(city)

	# Retrieve a city
	def get_city(self, city_index):
		return self.destination_cities[city_index]

	# Get number of cities in our tour
	def number_of_cities(self):
		return len(self.destination_cities)