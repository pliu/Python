# https://projecteuler.net/problem=87

from tools import findPrimes
from gmpy2 import isqrt


def prime_power_triple_count(n):
    """
    Returns the number of distinct integers below n that can be expressed as the sum of the square of a prime,
    the cube of a prime, and the fourth power of a prime
    """
    primes = findPrimes(int(isqrt(n)) + 1)
    prime_squares = []
    prime_cubes = []
    prime_fourths = []
    for prime in primes:
        product = prime * prime
        if product >= n:
            continue
        prime_squares.append(product)
        product *= prime
        if product >= n:
            continue
        prime_cubes.append(product)
        product *= prime
        if product < n:
            prime_fourths.append(product)
    count = 0
    seen = set()
    for fourth in prime_fourths:
        for cube in prime_cubes:
            first_sum = fourth + cube
            if first_sum >= n:
                break
            for square in prime_squares:
                second_sum = first_sum + square
                if second_sum >= n:
                    break
                if second_sum not in seen:
                    seen.add(second_sum)
                    count += 1
    return count


print(prime_power_triple_count(5*10**7))
