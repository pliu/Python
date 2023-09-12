# https://projecteuler.net/problem=3

from tools import findPrimes, findPrimeFactors
from gmpy2 import isqrt


def find_largest_prime_factor(n):
    primes = findPrimes(int(isqrt(n)) + 1)
    prime_factors = findPrimeFactors(primes, n)
    return prime_factors[-1]


print(find_largest_prime_factor(600851475143))
