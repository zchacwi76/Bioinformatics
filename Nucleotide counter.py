
>>> dna = "GATGGAACTTGACTACGTAAATT"

>>> 
>>> 
>>> from collections import defaultdict
>>> chars = defaultdict(int)
>>> for char in dna:
	chars[char] += 1

>>> print (chars)
defaultdict(<class 'int'>, {'G': 5, 'C': 3, 'T': 7, 'A': 8})
>>> 
