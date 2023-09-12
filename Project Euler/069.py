#https://projecteuler.net/problem=69

from tools import findPrimes
from tools import findPrimeFactors
from gmpy2 import isqrt

'''
Finds and returns the value of i that maximizes i/phi(i) (phi(i) is the number of integers less than
and coprime to i) for all i <= n
Method:
i/phi(i) = i/(i(1 - 1/p_1)(1 - 1/p_2)(1 - 1/p_3)...) = 1/((1 - 1/p_1)(1 - 1/p_2)(1 - 1/p_3)...) =
1/(((p_1 - 1)/p_1)(p_2 - 1)/p_2)(p_3 - 1)/p_3)...) = (p_1/(p_1 - 1))(p_2/(p_2 - 1))(p_3/(p_3 - 1))...
Since a prime factor with power greater than 1 increases i without increasing i/phi(i), if i has
prime factors with power greater than 1, then for i', the product of distinct prime factors of i,
i' < i and i/phi(i) = i'/phi(i'). Furthermore, because p/(p - 1) > 1 and is larger for smaller p,
maximizing (p_1/(p_1 - 1))(p_2/(p_2 - 1))(p_3/(p_3 - 1))... is achieved by selecting primes in
ascending order such that their product is smaller or equal to n.
Observation:
Runs in O(log(n)) time as opposed to the O(n*sqrt(n)) time of the below solution.
'''
def highestRatio(n):
    primesArray = findPrimes(int(isqrt(n)) + 1)
    currentProduct = 1
    for prime in primesArray:
        currentProduct *= prime
        if currentProduct > n:
            currentProduct /= prime
            return currentProduct

'''
Finds and returns the value of i that maximizes i/phi(i) (phi(i) is the number of integers less than
and coprime to i) for all i <= n
Method:
p**a = p*p**(a - 1). For every p elements, one is divisible by p and thus not coprime to p**a. Thus,
phi(p**a) = (p - 1)p**(a - 1). Given two numbers, x and y, and the sets of integers that are less
than and coprime to x and y, X and Y respectively, the set Z of integers that are less than and
coprime to z = xy is given by those integers that are coprime to both x and y (the set XY). Given
the prime decomposition of i, (p_1**a)(p_2**b)(p_3**c)..., then phi(i) = (1 - 1/p_1)p_1**a(1 - 1/p_2)
p**b(1 - 1/p_3)p_3**c... = i(1 - 1/p_1)(1 - 1/p_2)(1 - 1/p_3)...
'''
def highestRatioBrute(n):
    primesArray = findPrimes(int(isqrt(n)) + 1)
    currentMax = 0
    currentMaxValue = 0
    for i in range(1, n + 1):
        primeFactorsSet = set(findPrimeFactors(primesArray, i))
        check = i
        for primeFactor in primeFactorsSet:
            check *= (1 - 1.0/primeFactor)
        check = i/check
        if (check > currentMaxValue):
            currentMaxValue = check
            currentMax = i
    return currentMax

print(highestRatio(1000000))
print(highestRatioBrute(1000000))