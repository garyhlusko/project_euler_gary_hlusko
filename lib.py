#lib.py

from itertools import permutations

#functions needed for solving project euloer

def primes_between_numbers(a,b):
    primes_array = []
    for n in range(a,b+1):
        if is_prime(n):
            primes_array.append(n)
    return primes_array

def is_prime(n):
    #return a bolean if it's prime or not 
    return_boolean = True 
    # first step if it's even and not two it's not prime
    if(n == 2):
        return return_boolean
    elif (n % 2 == 0 ):
        return False
    # we want to iterate where i < n**.5 
    else: 
        i = 3
        while i <= n**.5:
            if n % i == 0:
                return False
            i = i + 1
        else:
            return True

def difference(n1,n2):
    return n2 - n1 

def array_difference_n_n1(array):
    return_array = []
    for i in range(0,len(array)-1):
        return_array.append(difference(array[i],array[i+1]))
    return return_array

def string_permutate(n):
    n = str(n)
    return_array = [''.join(p) for p in permutations(n)]
    return return_array

def switch_number(number):
	digits = list(str(number))
	digits = ''.join(digits[1:])+digits[0]
	return digits 
	
def iterate_sum_array(array):
    return_sums = []
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            return_sums.append(sum_parts_array(array,i,j))
        return return_sums
        
def sum_parts_array(array,n1,n2):
    return sum(array[n1:n2])