#!/usr/bin/python -tt
import toolbox
import convert
import config
import convert

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
    	n =  config.n
    	x,y = toolbox.cut_c(self._get_id(),n)
    	x = convert.bin2dec(x);
    	y = convert.bin2dec(y);
    	return toolbox.dist(x,y, config.EXPECTED_X, config.EXPECTED_Y)


