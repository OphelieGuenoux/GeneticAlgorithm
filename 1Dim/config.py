#!/usr/python

"""
COnfiguration file for global variables
"""
 
## ----------------------------------------- Dependencies-----------------------------------------------------------------------##

#EXPECTED_STR = [1,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,1,1,1]
EXPECTED_STR = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

#EXPECTED_X = 644
#EXPECTED_Y = 175
EXPECTED_X = 682
EXPECTED_Y = 682
# 0.0 = 0% and 1.0 = 100%
CHANCE_TO_MUTATE = 0.1
# high graduaded individu
GRADED_RETAIN_PERCENT = 0.2
# pourcentage de chance qu un faiblement gradee soit retenue
CHANCE_RETAIN_NONGRATED = 0.05

POPULATION_COUNT = 300
# nombre max de generation
GENERATION_COUNT_MAX = 300

# nb d individu haut grada a retenir
GRADED_INDIVIDUAL_RETAIN_COUNT = int(POPULATION_COUNT * GRADED_RETAIN_PERCENT)
# taille de la CdC a deviner
LENGTH_OF_EXPECTED_STR = len(EXPECTED_STR)
MIDDLE_LENGTH_OF_EXPECTED_STR = LENGTH_OF_EXPECTED_STR // 2
# valeur max de score qu un individu peut obtenir
MAXIMUM_FITNESS = LENGTH_OF_EXPECTED_STR
MIN_DIST = 0
# number for devide the individual in two part (x and y)
n= 2