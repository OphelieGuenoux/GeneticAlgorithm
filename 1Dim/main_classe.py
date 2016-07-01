#!/usr/bin/python -tt

## ------------------------------------------- dependencies ----------------------------------------------------------------- ##

import individual_class
import population_class
import config
import toolbox

import pygal
from random import random

## --------------------------------------------------------- MAIN ---------------------------------------------------------------------- ##

print (' -------------------------Genetique algorithms with classe 2D-----------------------------------------------')

# Create a population and compute starting grade
population = population_class.Population()
average_grade = population.average_population_grade()
print('Distance 1st population (average): %.2f' % average_grade)

# Make the population evolve
i = 0
solution = None
log_avg = []
while not solution and i < config.GENERATION_COUNT_MAX:
    population, average_grade, solution = population.evolve_population()
    if i & 3 == 3:
       print('Current Distance (average): %.2f' % average_grade, '(%d generation)' % i)
    if i & 3 == 3:
       log_avg.append(average_grade)
    i += 1

# plot the fitness chart 
line_chart = pygal.Line(show_dots=False, show_legend=False)
line_chart.title = 'Fitness evolution'
line_chart.x_title = 'Generations'
line_chart.y_title = 'Fitness'
line_chart.add('Fitness', log_avg)
line_chart.render_to_file('bar_chart.svg')

# Print the final stats
average_grade = population.average_population_grade()
print('Final Distance (average): %.2f' % average_grade)

# Print the solution

if solution:
    print('Solution found (%d times) after %d generations.' % (len(solution), i))
    print solution
else:
    print('No solution found after %d generations.' % i)
