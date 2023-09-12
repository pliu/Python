#https://projecteuler.net/problem=46

from tools import findPrimes

'''
Finds and returns the lowest composite odd, x, that does not satisfy x = p + 2*y**2 where p is a
prime and y is an integer
'''
def findLowestNonGoldbachOdd():

    # Guessed x < 1000000, so would only need primes up to 1000000
    primesArray = findPrimes(1000000)

    primesSet = set(primesArray)
    check = 35
    while True:
        if check not in primesSet:
            i = 1
            isGoldbachOdd = False

            '''
            Optimization: Checking i such that 2*i**2 < check checks approximately sqrt(check)
            values whereas checking i such that primesArray[i] < check checks approximately
            check/ln(check) values.
            '''
            while (2*i**2 < check):
                diff = check - 2*i**2
                if diff in primesSet:
                    isGoldbachOdd = True
                    break
                i += 1
            if not isGoldbachOdd:
                return check
        check += 2

print findLowestNonGoldbachOdd()
