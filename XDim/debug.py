#!/usr/python

"""
file for testing some toolbox function
"""

import toolbox
import config

print('cutting function test')
a = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
print toolbox.cut_c(a,4)

EXPECTED_BIT = toolbox.cut_c(config.EXPECTED_STR, config.N)
print ('EXPECTED_BIT')
print EXPECTED_BIT
EXPECTED_NUMBER = toolbox.bin2dec_tab(EXPECTED_BIT)
print ('expected number')
print EXPECTED_NUMBER