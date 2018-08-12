Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dna = "GATGGAACTTGACTACGTAAATT"
>>> >>> from collections import defaultdict
>>> chars = defaultdict(int)
>>> for char in dna:
	chars[char] += 1

>>> print chars
SyntaxError: invalid syntax
>>> from collections import defaultdict
>>> chars = defaultdict(int)
>>> for char in dna:
	chars[char] += 1

>>> print chars
SyntaxError: multiple statements found while compiling a single statement
>>> from collections import defaultdict
chars = defaultdict(int)
for char in dna:
	chars[char] += 1

print chars
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> from collections import defaultdict
>>> chars = defaultdict(int)
>>> for char in dna:
	chars[char] += 1

>>> print (chars)
defaultdict(<class 'int'>, {'G': 5, 'C': 3, 'T': 7, 'A': 8})
>>> 
