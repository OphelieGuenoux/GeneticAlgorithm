#!/usr/bin/python -tt
import toolbox
import convert
import config
import convert
import numpy
import math

## --------------------------------------------------------------- global variables ----------------------------------------------------- ##

EXPECTED_BIT = toolbox.cut_c(config.EXPECTED_STR, config.N)
EXPECTED_NUMBER = toolbox.bin2dec_tab(EXPECTED_BIT)

## ---------------------------------------------------------------------------------------------------------------------------------------- ##
class Individual(object):
    """ individual belong to a population 

    Attribute : 
    - id : bit code
    """
    ##------------------------------------------------getter--------------------------------------------------##

    def _get_id(self):
    	""" return the bitcode for the current individual """
    	return self._id

    ## -------------------------------------------------------------------------------------------------------##

    def __init__(self, *args):
    	""" return an individual object with bitcode, fitness, and chance to be choose """
        if args:
            self._id = args[0]
        else :
    	   self._id = toolbox.get_random_individual()

    ##------------------------------------------------functions-----------------------------------------------##
    def compute_individual_fitness(self):
    	""" Compute the fitness of the given individual. """
    	X = toolbox.cut_c(self._get_id(),config.N)
        X_dec = toolbox.bin2dec_tab(X)
        dist = []
        for pos in range (0,len(X_dec),2):
            dist.append(toolbox.dist(X_dec[pos], X_dec[pos+1], EXPECTED_NUMBER[pos], EXPECTED_NUMBER[pos+1]))

        return numpy.mean(dist)

    def compute_individual_fitnessG(self):
        """ Compute Griewangk function of the given individual. """
        X = toolbox.cut_c(self._get_id(),config.N)
        X_dec = toolbox.bin2dec_tab(X)
        G = math.pow(X_dec[0],2)/4000 + math.pow(X_dec[1],2)/4000 - (math.cos(X_dec[0]) * math.cos(X_dec[1]/2)) + 1
        return G

    def compute_individual_fitnessP(self):
	""" Compute Paraboloid function of the given individual. """
	X = toolbox.cut_c(self._get_id(),config.N)
	X_dec = toolbox.bin2dec_tab(X)
	P = math.pow(X_dec[0],2) + math.pow(X_dec[1],2)
        return P
