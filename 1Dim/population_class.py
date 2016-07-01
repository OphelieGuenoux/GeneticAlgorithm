#!/usr/bin/python -tt

from individual_class import Individual
import config
import toolbox
import random
import convert
import math

class Population(Individual):
    """ a population is a set of individual

    Attribute : 
    - population : array of individual
    - selection_chance : array with i = individual and give the chance for each individual to be choose
    - graded_population : a list of tuple (individual, fitness) sorted from the most gradded to less graded
    """

    ## --------------------------------------------------------------------------------------------------------------------------------##
    def __init__(self, *args):
        """ return a population with individual array, an array of selection_chance and grade population """
        if args :
            self._population = args[0]
        else :
            self._population = self.create_population()

        self._graded_population = self.grade_population()
        self._selection_chance = self.calculate_chance()


    ## ---------------------------------------------------------- getter ------------------------------------------------------- ##
    def _get_selection_chance(self):
    	return self._selection_chance

    def _get_graded_population(self):
    	return self._graded_population

    def _get_population_id(self):
        population_id = []
        for individual in self._population:
            population_id.append(individual._get_id())
        return population_id

    ## ------------------------------------------------------------ functions ------------------------------------------------------- ##

    def create_population(self):
        """ Create a new random population, made of `POPULATION_COUNT` individual. """
        return [Individual() for _ in range(config.POPULATION_COUNT)]

    def max_distance (self):
    	""" return the worse individual in the graded population """
        graded_population = self._get_graded_population()
    	individual_worse, maximum_distance = graded_population[0]
    	return maximum_distance

    def calculate_chance(self):
    	""" Calculate the chance for each individual to be choose """
    	maximum_distance = self.max_distance()
        grade_population = self._get_graded_population()
    	selection_chances = []
        for individual, fitness in grade_population:
            selection_chance = abs(1-(fitness/maximum_distance))
            selection_chances.append(selection_chance)
        return selection_chances

    def calculate_sum(self):
    	""" Calculate the sum of each elements in the choice array """
    	selection_chances = self._get_selection_chance()
    	total = 0
    	for chance in selection_chances:
    		total += chance
    	return total

    def grade_population(self):
    	""" Grade the population. Return a list of tuple (individual, fitness) sorted from most graded to less graded. """
    	graded_individual = []
    	for individual in self._population:
			graded_individual.append((individual, individual.compute_individual_fitness()))
    	return sorted(graded_individual, key=lambda x: x[1], reverse=True)

    def select_parent(self):
    	""" Select parent from the last generation for the next one, return an individual """
        selection_chances = self._get_selection_chance()
    	sum_chance = self.calculate_sum()
    	number = random.random()*sum_chance
    	index = 0
    	position = selection_chances[index]
    	while position <= number and index < len(selection_chances)-1:
    		index = index+1
    		position += selection_chances[index]
        return self._population[index]

    def select_parents(self, desired_len):
    	""" select parents """
    	selection_chances = self._get_selection_chance()
    	return [self.select_parent() for _ in range(desired_len)*2]

    def average_population_grade(self):
    	""" Return the average fitness of all individual in the population. """
    	total = 0
    	for individual in self._population:
    		total += individual.compute_individual_fitness()
    	return total / config.POPULATION_COUNT


    def evolve_population(self):
    	""" Make the given population evolving to his next generation. """
    	 
    	# Get individual sorted by grade (top first), the average grade and the solution (if any)
    	raw_graded_population = self._get_graded_population()
    	selection_chances = self._get_selection_chance()
    	average_grade = 0
    	solution = []
    	graded_population = []
    	for individual, fitness in raw_graded_population:
    		average_grade += fitness
    		graded_population.append(individual)
    		if fitness == config.MIN_DIST: 
    			solution.append(individual)
    	average_grade /= config.POPULATION_COUNT
     
    	# End the script when solution is found
    	if solution:
    		return self, average_grade, solution    
     
    	# Filter the top graded individuals
    	parents = graded_population[len(raw_graded_population)-config.GRADED_INDIVIDUAL_RETAIN_COUNT:]

        # get parents id
        parents_id = toolbox.object_to_id(parents)

    	parents_best_len = len(parents)
    	desired_len = config.POPULATION_COUNT - parents_best_len
    	parents_random = self.select_parents(desired_len)

    	# Crossover parents to create children
    	parents_len = len(parents_random)
    	desired_len = config.POPULATION_COUNT*2 - parents_len

        # get parents_random id
        parents_random_id = toolbox.object_to_id(parents_random)

    	children = []
    	i = 0
        while i < len(parents_random):
            father = parents_random_id[i]
            mother = parents_random_id[i+1]
            i = i+2
            child = Individual(father[:config.MIDDLE_LENGTH_OF_EXPECTED_STR] + mother[config.MIDDLE_LENGTH_OF_EXPECTED_STR:])
            children.append(child)

        # get the children id
        children_id = toolbox.object_to_id(children)

    	# Mutate some individuals
    	for individual_id in children_id:
    		if random.random() < config.CHANCE_TO_MUTATE:
    			place_to_modify = int(random.random() * config.LENGTH_OF_EXPECTED_STR)
    			if individual_id[place_to_modify] == 0:
    				individual_id[place_to_modify] = 1
    			else :
    				individual_id[place_to_modify] = 0
    	
    	# add children with best parents and create new population
    	parents_id.extend(children_id)
        ind = []
        for individual in parents_id:
            ind.append(Individual(individual))
    	new_population = Population(ind)

    	return new_population, average_grade, solution
