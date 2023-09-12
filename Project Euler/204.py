# https://projecteuler.net/problem=204

from tools import findPrimes
from copy import deepcopy


COUNT = 0
MAX_CHECK = 0
PRIMES = []


# TODO: Make faster
def generalized_hamming_count(max_check, n):
    global MAX_CHECK
    global PRIMES
    MAX_CHECK = max_check
    PRIMES = findPrimes(n + 1)
    current_exponents = [0 for _i in PRIMES]
    recursive_check_exponents(1, current_exponents, 0)


def recursive_check_exponents(current_product, current_exponents, index):
    if index == len(current_exponents):
        global COUNT
        COUNT += 1
        return
    next_product = current_product
    next_exponents = deepcopy(current_exponents)
    i = 0
    while True:
        next_exponents[index] = i
        if next_product > MAX_CHECK:
            return
        recursive_check_exponents(next_product, next_exponents, index + 1)
        next_product *= PRIMES[index]
        i += 1


generalized_hamming_count(10**9, 100)
print(COUNT)
