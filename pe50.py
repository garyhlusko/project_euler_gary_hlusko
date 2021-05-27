# project euler 50

'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

from lib import primes_between_numbers,is_prime
from progess_bar import update_progress

def pe_50():
    greatest_sum = 0
    greatest_len = 0
    sequence = 0
    prime_consecutive_array = primes_between_numbers(2,999999)
    max_possible_length = len(prime_consecutive_array)
    k = max_possible_length
    i = 0
    j = i + 1
    while k >= j:
        for i in range(i,max_possible_length):
            for j in range(k,j,-1):
                if j-i >= greatest_len:
                    sequence_array = prime_consecutive_array[i:j]
                    sum_sequence_array = sum(sequence_array)
                    if sum_sequence_array < 1000000:
                        if is_prime(sum_sequence_array) and len(sequence_array) > greatest_len:
                            greatest_len = len(sequence_array)
                            greatest_sum = sum_sequence_array
                            sequence = sequence_array
                            print(sum_sequence_array,greatest_len)
        i = i + 1
        j = j + 1
        k = k - 1
    print(greatest_sum,greatest_len,sequence)
    
if __name__ == "__main__":
    pe_50()