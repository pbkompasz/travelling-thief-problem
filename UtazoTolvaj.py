import numpy as np
import math
import matplotlib.pyplot as plt
import copy
import random
import time
import sys
from decimal import *

getcontext().prec = 3

class Item:

    def __init__(self, value, weight, taken):
        self.value = value
        self.weight = weight
        self.taken = taken

    def __str__(self):
        return ("Ertek: " + str(self.value) + " suly: " + str(self.weight) + "\n")

    def __eq__(self, other):
        if (self.value == other.value and self.weight == other.weight):
            return True
        return False

    def take_item(self):
        """
        docs
        """
        self.taken = True

    def return_item(self):
        """
        docstring
        """
        self.taken = False

class City:

    items = np.empty(0)

    def __init__(self, x, y, visited):
        self.x = x
        self.y = y
        self.visited = visited

    def __str__(self):
        if (self.visited):
            visited_msg = " visited "
        else:
            visited_msg = " not visited "

        resp =  "x: " + str(self.x) + " ,y: " + str(self.y) + visited_msg + "\n"

        for item in self.items:
            resp += str(item)

        return resp

    def distance(self, other):
        """
        Returns distance from a different city
        """
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2) 

    def visit(self):
        """
        Unvisite all cities, start from scratch
        """
        self.visited = True

    def unvisit(self):
        """
        Unvisite all cities, start from scratch
        """
        self.visited = False

    def add_item(self, item):
        """
        Unvisite all cities, start from scratch
        """
        self.items = np.append(self.items, item)

    def take_item(self, item):
        """
        Unvisite all cities, start from scratch
        """
        pos = -1
        for i in self.items:
            if i == item:
                i.take_item()
                break

class UtazoTolvaj:

    bag = np.empty(0)
    cities = np.empty(0)
    route = np.empty(0)
    weight = 0
    value = 0
    

    population_size = None
    no_of_variables = None
    sol_per_pop = None
    population_size = None
    num_parents_mating = None
    num_offspring = None
    population = None

    def __init__(self, filename, iteration):
        self.filename = filename
        self.iteration = iteration
        self.read_inputs(filename)

    def read_inputs(self, filename):
        """
        Unvisite all cities, start from scratch
        """
        # File structure:
            # 1st line: Maximum weight, Minimum price, Number of cities
            # Line for each city: x coordinate, y coodinate, number of items
            # Line for each ites: weight of item, value of item

        file1 = open('./' + filename, 'r') 
        print('Reading from file: ' + filename)

        line = file1.readline().rstrip().split(' ')
        self.weight = int(line[0])
        self.value = int(line[1])
        n = int(line[2])

        for i in range(n):
            line = file1.readline().rstrip().split(' ')
            x = int(line[0])
            y = int(line[1])
            m = int(line[2])
            city = City(x, y, False)
            for j in range(m):
                line = file1.readline().rstrip().split(' ')
                weight = int(line[0])
                value = int(line[1])
                city.add_item(Item(weight, value, False))
            self.add_city(city)

    def __str__(self):
        resp = "Taskaban levok termekek szama: " + str(len(self.bag)) + "\n"
        for item in self.bag:
            resp += str(item)
        resp += "Varosok: " + str(len(self.cities)) + "\n"
        for city in self.cities:
            resp += str(city)
        resp += "Ut: " + str(len(self.route)) + "\n"
        for city in self.route:
            resp += str(city)
        


        return resp
    
    def add_city(self, city):
        """
        Unvisite all cities, start from scratch
        """
        self.cities = np.append(self.cities, city)

    def add_item(self, item):
        """
        Unvisite all cities, start from scratch
        """
        self.bag = np.append(self.bag, item)

    def take_item(self, city, item):
        """
        Unvisite all cities, start from scratch
        """
        for t in self.cities:
            if (t == city):
                t.take_item(item)
                return

    def remove_item(self, item):
        """
        Unvisite all cities, start from scratch
        """
        for i in range(len(self.bag)):
            if (self.bag[i] == other):
                self.bag = np.delete(self.bag, i)
                break


    def get_distance(self, route):
        """
        Unvisite all cities, start from scratch
        """
        distance = 0
        for i in range(len(route)-1):
            if route[i] == None or route[i+1] == None: 
                distance += 0
            else:
                distance += route[i].distance(route[i+1])
        return distance

    def get_weight(self, bag):
        """
        Unvisite all cities, start from scratch
        """
        weight = 0
        for item in bag:
            weight += item.weight 
        return weight

    def get_value(self, bag):
        """
        Unvisite all cities, start from scratch
        """
        value = 0
        for item in bag:
            value += item.value 
        return value

    def unvisit_all_cities(self):
        """
        Unvisite all cities, start from scratch
        """
        self.route = np.empty(0)
        for city in self.cities:
            city.unvisit()

    def return_all_items(self):
        """
        docstring
        """
        for city in self.cities:
            for item in city.items:
                item.return_item()

    def visit_city(self, other):
        """
        docstring
        """
        for city in self.cities:
            if (city == other):
                city.visit()

    def get_random_unvisited_city(self):
        """
        docstring
        """
        found = False
        while (not found):
            random_city = self.cities[random.randrange(len(self.cities))]
            if (not random_city.visited):
                return random_city
            

    def generate_random_route(self):
        """
        Generates a random route
        """

        self.unvisit_all_cities()
        starting_city = self.cities[0]
        self.visit_city(starting_city)
        visited_cities = 1
        random_route = np.empty(0)
        random_route = np.append(random_route, starting_city)
        while (visited_cities < len(self.cities)):
            random_city = self.get_random_unvisited_city()
            self.visit_city(random_city)
            random_route = np.append(random_route, random_city)
            visited_cities += 1
        
        random_route = np.append(random_route, starting_city)
        return random_route

    def get_random_untaken_item(self):
        """
        docstring
        """
        found = False
        while (not found):
            random_city = self.cities[random.randrange(len(self.cities))]
            random_item = random_city.items[random.randrange(len(random_city.items))]
            if (not random_item.taken):
                return random_city, random_item

    def generate_random_bag(self):
        """
        Generates a random bag
        """
        self.return_all_items()
        weight = 0
        value = 0
        random_bag = np.empty(0)
        fail = 0
        found = False
        not_found_fail = 0
        while (not found):
            while(value < self.value):
                random_city, random_item = self.get_random_untaken_item()
                if (weight + random_item.weight <= self.weight):
                    self.take_item(random_city, random_item)
                    weight += random_item.weight
                    value += random_item.value
                    random_bag = np.append(random_bag, random_item)
                    fail = 0
                else:
                    fail += 1

                if (fail>10):
                    self.return_all_items()
                    random_bag = np.empty(0)
                    weight = 0
                    value = 0
            if (value >= self.value):
                return random_bag
            else:
                not_found_fail += 1
                fail = 100
            
            if (not_found_fail>5):
                print("No possible combination of items found!")
                return np.empty(0)

    def visualize(self):
        """
        Visualization of current route using mathplotlib
        """
        for city in self.cities:
            plt.scatter(city.x, city.y, c='b')
        x = []
        y = []
        for point in self.route:
            x.append(point.x)
            y.append(point.y)
        plt.plot(x, y, c='b')
        plt.ylabel('Utazo tolvaj')
        plt.draw()
        plt.show()
    
    def decrease_temperature(self, temperature_origin, k):
        """
        docstring
        """
        alpha = random.uniform(0.8, 0.9)
        return temperature_origin * pow(0.9, k)

    def quality_route(self, route):
        """
        docstring
        """
        return -1*self.get_distance(route)

    def quality_bag(self, bag):
        """
        docstring
        """
        return self.get_value(bag)

    def modify_route(self, route):
        """
        docstring
        """
        return self.generate_random_route()

    def modify_bag(self, bag):
        """
        docstring
        """
        modified_bag = self.generate_random_bag()
        if modified_bag.size == 0:
            return bag
        return modified_bag
        

    def simulated_annealing(self):
        
        temperature_origin = 1000000000000000000000000 
        temperature = 1000000000000000000000000
        
        it = 0
        stop = self.iteration
        
        random_route = self.generate_random_route()
        best_route = copy.copy(random_route)

        random_bag = self.generate_random_bag()
        best_bag = copy.copy(random_bag)

        while temperature>0 and it<stop:
            it += 1
            # Finding route
            random_route_ = copy.copy(random_route)
            modified_random_route = self.modify_route(random_route_)
            random_generated_number = random.uniform(0, 1)
            if (self.quality_route(modified_random_route) < self.quality_route(random_route) or random_generated_number < Decimal(Decimal(math.e) ** Decimal((self.quality_route(modified_random_route) - self.quality_route(random_route)) / temperature)) ):
                random_route = copy.copy(modified_random_route)
            if (self.quality_route(random_route) > self.quality_route(best_route)):
                best_route = copy.copy(random_route)
                print("New best route! " + str(self.get_distance(best_route))) 

            # Finding bag
            random_bag_ = copy.copy(random_bag)
            modified_random_bag = self.modify_bag(random_bag_)
            random_generated_number = random.uniform(0, 1)
            if (self.quality_bag(modified_random_bag) < self.quality_bag(random_bag) or random_generated_number < Decimal(Decimal(math.e) ** Decimal((self.quality_bag(modified_random_bag) - self.quality_bag(random_bag)) / temperature)) ):
                random_bag = copy.copy(modified_random_bag)
            if (self.quality_bag(random_bag) > self.quality_bag(best_bag)):
                best_bag = copy.copy(random_bag)
                print("New best bag!") 
        
            temperature = self.decrease_temperature(temperature_origin, it)
        
        self.route = copy.copy(best_route)
        self.bag = copy.copy(best_bag)

    def mating_pool(self, minimize, maximize):
        """
        docstring
        """
        parents = np.empty(self.num_parents_mating, dtype=City)
        fitness = np.empty(self.sol_per_pop)
        for i in range(len(fitness)):
            fitness[i] = -1*self.quality_route(self.population[i])
        for parent_num in range(self.num_parents_mating):
            if minimize:
                min_fitness_idx = np.where(fitness == np.max(fitness))
                min_fitness_idx = min_fitness_idx[0][0]
                parents[parent_num] = self.population[min_fitness_idx]
                fitness[min_fitness_idx] = -99999999999
            else:
                max_fitness_idx = np.where(fitness == np.min(fitness))
                max_fitness_idx = max_fitness_idx[0][0]
                parents[parent_num, :] = self.population[max_fitness_idx, :]
                fitness[max_fitness_idx] = 99999999999

        return parents

    def mating(self, parents):
        """
        docstring
        """
        
        offspring = np.empty(self.num_offspring, dtype=City)
        crossover_point = int(self.no_of_variables / 2)
        # Uj populacio fele utodok fele szulokbol a legjobbak
        for i in range(0, len(offspring)):
            offspring[i] = np.append(offspring[i], parents[i%len(parents)])

            offspring[i] = np.delete(offspring[i], 0)

        return offspring

    def mutation(self, offspring_crossover):
        """
        docstring
        """
        for idx in range(len(offspring_crossover)-1):
            random_pos1 = random.randint(1, self.no_of_variables - 1)        
            random_pos2 = random.randint(1, self.no_of_variables - 1)
            while random_pos1 == random_pos2:
                random_pos1 = random.randint(0, self.no_of_variables - 1)        
                random_pos2 = random.randint(0, self.no_of_variables - 1)

            offspring_crossover[idx][random_pos1], offspring_crossover[idx][random_pos2] = offspring_crossover[idx][random_pos2], offspring_crossover[idx][random_pos1]
        return offspring_crossover


    def new_generation(self, parents, mutated_offspring):
        """
        docstring
        """
        new_population = np.empty(self.sol_per_pop, dtype=City)
        new_population[0:len(parents)] = parents
        new_population[(len(parents)):] = mutated_offspring
        return new_population

    def best_solution(self, new_generation, minimize, maximize):
        """
        docstring
        """
        comp = new_generation[0]
        for gen in new_generation:
            if minimize:
                if -1*self.quality_route(gen) < -1*self.quality_route(comp):
                    comp = gen
            else:
                if -1*self.quality_route(gen) > -1*self.quality_route(max):
                    comp = gen
        return comp

    def genetic(self, no_cromosome):
        """
        docstring
        """
        num_generations = 5000
        self.no_of_variables = len(self.cities)+1
        self.sol_per_pop = no_cromosome
        self.population_size = (self.sol_per_pop, self.no_of_variables)
        self.num_parents_mating = int(self.sol_per_pop / 2)
        self.num_offspring = self.sol_per_pop - self.num_parents_mating
        self.population = np.empty(self.sol_per_pop, dtype=(City))
        for i in range(self.sol_per_pop):
            self.population[i] = self.generate_random_route()

        best_generation = None
        best = None

        for i in range(0, num_generations):    
            parents = copy.copy(self.mating_pool(True, False))
            offspring = copy.copy(self.mating(parents))
            mutated_offspring = copy.copy(self.mutation(offspring))
            new_generation = copy.copy(self.new_generation(parents, mutated_offspring))
            best_generation = copy.copy(self.best_solution(new_generation, True, False)) 
            self.population = new_generation
            if i == 0:
                best = best_generation
            # print(self.quality_route(best_generation), self.quality_route(best))
            if self.quality_route(best_generation) > self.quality_route(best):
                print(self.quality_route(best))
                best = best_generation

        
        self.route = copy.copy(best)

print(sys.argv)
ut = UtazoTolvaj(sys.argv[1], int(sys.argv[2]))
# ut.genetic(12)
ut.simulated_annealing()
print(ut.get_value(ut.bag))
print(ut)
ut.visualize()