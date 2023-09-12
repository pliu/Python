#https://projecteuler.net/problem=95

from tools import findPrimes
from tools import findDivisors
from gmpy2 import isqrt

'''
Recursively finds and returns the amicable loop that i is a member of given that the loop exists and
no members of the loop exceed n
'''
def followSumDivisors(primesArray, currentChain, visited, i):

    #Base case: If i > n, it cannot be part of an amicable loop with no members greater than n
    if i > len(visited) - 1:
        return None

    #Base case: If i was visited in a previous chain, it cannot lead to any new loops
    if visited[i]:
        return None

    '''
    If i was seen before in the current chain, then it belongs to an amicable loop. Not all elements
    in currentChain are necessarily members of the loop, however, so another pass is made to
    determine which ones are.
    '''
    if i in currentChain:
        loop = set()
        while i not in loop:
            loop.add(i)
            i = sum(findDivisors(primesArray, i))
        return loop

    currentChain.add(i)
    result = followSumDivisors(primesArray, currentChain, visited, int(sum(findDivisors(primesArray, i))))

    '''
    It is important to set i to visited when unwinding the recursive stack because whether i was
    visited in a previous chain is checked before whether i has been seen in the current chain
    '''
    visited[i] = True

    return result

'''
Finds and returns the lowest element of the longest amicable loop whose members do not exceed n (an
amicable loop is one such that iteratively summing the proper divisors of a number leads back to
that number).
'''
def findLowestLongestAmicableLoop(n):
    maxLoopLength = 0
    visited = [False for _i in range(n + 1)]
    primesArray = findPrimes(int(isqrt(n)) + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            currentChain = set()
            loop = followSumDivisors(primesArray, currentChain, visited, i)
            if loop and len(loop) > maxLoopLength:
                maxLoopLength = len(loop)
                maxLoop = loop
    return min(maxLoop)

print(findLowestLongestAmicableLoop(10**6))
