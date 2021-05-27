# project euler project 49

'''
	The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

	There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

	What 12-digit number do you form by concatenating the three terms in this sequence?
'''

from lib import string_permutate,is_prime,array_difference_n_n1,primes_between_numbers


def pe_49(): 
	primes = primes_between_numbers(1000,10000)
	for i in range(0,len(primes)):
		permutated_prime = string_permutate(primes[i])
		permutated_prime = [int(x) for x in permutated_prime]
		for j in range(i+1,len(primes)):
			if primes[j] in permutated_prime:
				n1 = primes[j]+(primes[j]-primes[i]) 
				if n1 < 10000 and is_prime(n1) and n1 in permutated_prime:
					print(primes[i],primes[j],n1)

if __name__ == "__main__":
	pe_49()