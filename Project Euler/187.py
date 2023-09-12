# https://projecteuler.net/problem=187

from tools import findPrimes


def get_num_semiprimes(n):
    """
    Finds the number of integers between 1 and n that are the product of two primes.
    Method:
    Finds all primes up to n/2 and returns them in an ascending list. Walk the list in ascending
    order and for each element, find the highest element (by walking the list in descending order,
    never resetting since if b is the largest number such that a * b <= n, when c > a, if d is the
    largest number such that c * d <= n, then d <= b, otherwise a * d <= n and b would not be the
    largest number such that a * b <= n) such that their product is less than or equal to n.
    """
    primes = findPrimes(int(n/2))
    start_index = 0
    end_index = len(primes) - 1
    count = 0
    while True:
        while primes[start_index] * primes[end_index] >= n:
            end_index -= 1
        if end_index < start_index:
            break
        count += end_index - start_index + 1
        start_index += 1
    return count


print(get_num_semiprimes(10**8))
