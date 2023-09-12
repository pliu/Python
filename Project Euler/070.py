#https://projecteuler.net/problem=70

from tools import isPermutation
from tools import findPrimes
from tools import findPrimeFactors
from tools import checkPrime
from gmpy2 import isqrt

'''
Finds and returns Euler's totient function of n (the number of integers coprime to and less than n)
given the set of n's distinct prime factors
'''
def findPhi(primesSet, n):
    phi = n
    for primeFactor in primesSet:
        phi *= (1 - 1.0/primeFactor)
    return phi

#Given an array of primes up to n, inclusive, finds and returns the next prime greater than n
def nextPrime(primesArray, n):
    check = n + 1
    while not checkPrime(primesArray, check):
        check += 1
    return check

# TODO
'''
Finds and returns i < n such that phi(i) is a permutation of i and which minimizes i/phi(i)
Method:
i/phi(i) = i/(i(1 - 1/p_1)(1 - 1/p_2)(1 - 1/p_3)...) = 1/((1 - 1/p_1)(1 - 1/p_2)(1 - 1/p_3)...) =
1/(((p_1 - 1)/p_1)(p_2 - 1)/p_2)(p_3 - 1)/p_3)...) = (p_1/(p_1 - 1))(p_2/(p_2 - 1))(p_3/(p_3 - 1))...
Minimizing (p_1/(p_1 - 1))(p_2/(p_2 - 1))(p_3/(p_3 - 1))... is equivalent to maximizing
((p_1 - 1)/p_1)((p_2 - 1)/p_2)((p_3 - 1)/p_3)... As (p - 1)/p < 1
- show that this is achieved when there are only two prime factors
- show a lower bound on the values needing to be tested (for both primes and the composite)
'''
def findLowestPhiPermutation(n):
    primesArray = findPrimes(int(isqrt(n)) + 1)
    lower = len(primesArray) - 1
    while True:
        current = len(primesArray) - 1
        while current >= lower:
            check = primesArray[lower]*primesArray[current]
            if check < n:
                primesSet = set()
                primesSet.add(primesArray[lower])
                primesSet.add(primesArray[current])
                if isPermutation(check, int(findPhi(primesSet, check))):
                    return check, primesArray[lower], primesArray[current]
            current -= 1
        lower -= 1
        while primesArray[lower]*primesArray[len(primesArray) - 1] < n:
            primesArray.append(nextPrime(primesArray, primesArray[len(primesArray) - 1]))

#Finds and returns i < n such that phi(i) is a permutation of i and which minimizes i/phi(i)
def findLowestPhiPermutationBrute(n):
    primesArray = findPrimes(int(isqrt(n)) + 1)
    currentMin = 0
    currentMinValue = n
    i = n
    while i > 1:
        primesSet = findPrimeFactors(primesArray, i)
        phi = findPhi(primesSet, i)
        check = i/phi
        if check < currentMinValue:
            if isPermutation(i, int(phi)):
                currentMinValue = check
                currentMin = i
                print(primesSet)
        i -= 1
    return currentMin

print(findLowestPhiPermutation(10**7))
print(findLowestPhiPermutationBrute(10**7))
