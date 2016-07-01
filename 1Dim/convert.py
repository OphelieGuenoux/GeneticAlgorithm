#!/usr/python

def bin2dec(b):
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

def main():
    """ Main function. """
    b = input('enter a binary code to convert')
    rslt = bin2dec(b)
    print rslt

if __name__ == '__main__':
    main()
  
