# this tests the scripts that i made

import lib

def test_is_prime(n):
    for number in range(2,n+1):
        if lib.is_prime(number):
            print("{} is prime".format(number))


if __name__ == "__main__":
    test_is_prime(10000)