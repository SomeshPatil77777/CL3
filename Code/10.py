import numpy as np
import random

# Define the distance matrix (example: 4 cities)
distance_matrix = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])

# ACO parameters
num_ants = 10
num_iterations = 50
evaporation_rate = 0.5
pheromone_constant = 1.0
heuristic_constant = 1.0

num_cities = len(distance_matrix)

# Initialize pheromone and visibility matrices
pheromone = np.ones((num_cities, num_cities))
visibility = 1 / (distance_matrix + np.eye(num_cities))  # avoid divide by 0 on diagonal

# ACO algorithm
best_route = None
shortest_distance = float("inf")

for iteration in range(num_iterations):
    ant_routes = []
    
    for ant in range(num_ants):
        current_city = random.randint(0, num_cities - 1)
        visited_cities = {current_city}
        route = [current_city]

        while len(visited_cities) < num_cities:
            probabilities = []
            total = 0

            for city in range(num_cities):
                if city not in visited_cities:
                    pher = pheromone[current_city][city] ** pheromone_constant
                    vis = visibility[current_city][city] ** heuristic_constant
                    prob = pher * vis
                    probabilities.append((city, prob))
                    total += prob

            if total == 0:
                next_city = random.choice([city for city in range(num_cities) if city not in visited_cities])
            else:
                # Normalize and select city based on probability
                probabilities = [(city, prob / total) for city, prob in probabilities]
                r = random.random()
                cumulative = 0.0
                for city, prob in probabilities:
                    cumulative += prob
                    if r <= cumulative:
                        next_city = city
                        break

            route.append(next_city)
            visited_cities.add(next_city)
            current_city = next_city

        ant_routes.append(route)

    # Pheromone update
    delta_pheromone = np.zeros((num_cities, num_cities))

    for route in ant_routes:
        distance = sum(distance_matrix[route[i]][route[(i + 1) % num_cities]] for i in range(num_cities))
        for i in range(num_cities):
            a, b = route[i], route[(i + 1) % num_cities]
            delta_pheromone[a][b] += 1 / distance
            delta_pheromone[b][a] += 1 / distance  # symmetrical TSP

        if distance < shortest_distance:
            shortest_distance = distance
            best_route = route

    pheromone = (1 - evaporation_rate) * pheromone + delta_pheromone

# Output the best route and its distance
print("Best route:", best_route)
print("Shortest distance:", shortest_distance)
