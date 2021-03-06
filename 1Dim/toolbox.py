#!/usr/python

"""
Toolbox with usefull functions
"""

## ------------------------------------------------------ Dependencies -------------------------------------------------------##

import config
import random 
import math

## ------------------------------------------------------- Random ----------------------------------------------------------- ##
def get_random_bit():
    """ Return a random bit """
    return random.randint(0,1)

def get_random_individual():
	""" Create a new random individual. """
   	return [get_random_bit() for _ in range(config.LENGTH_OF_EXPECTED_STR)]

def get_random_population():
    """ Create a new random population, made of `POPULATION_COUNT` individual. """
    return [get_random_individual() for _ in range(config.POPULATION_COUNT)]

## --------------------------------------------------------- Operations -------------------------------------------------------##

def cut_c(tab,n):
    """ cut the bitcode c into 2 differents bitcode """
    x = tab[0:len(tab)/n]
    y = tab[len(tab)/n: len(tab)]
    return x,y 

def dist(x1,y1,x2,y2):
	""" calculate the squared distance between two differents points """
   	return math.hypot(x2-x1, y2-y1)


def bin2dec(b):
	""" turn a bitcode into a decimal number """
	i=0
	n=len(b)
	puissance=0
	index=-1
	while index>=-n:
		if b[index]==1:
			i= i + 2**puissance
		puissance= puissance +1
		index=index-1
	return i

def object_to_id(the_object):
	parents_id = []
	for individual in the_object:
		parents_id.append(individual._get_id())
	return parents_id