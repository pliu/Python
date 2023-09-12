# https://projecteuler.net/problem=173

from gmpy2 import isqrt


def get_num_hollow_sq_laminae(max_tiles):
    """
    Returns the number of squares that can be formed by adding shells around an inner, empty square such that at most
    max_tiles are used
    Method:
    For each inner, empty square of some length, the maximum number of shells (and consequently the number of solutions
    for the given inner square) is given by:
    tiles_used = outer_diameter^2 - inner_length^2 <= max_tiles
    outer_length = inner_length + 2 * num_shells
    (inner_length + 2 * num_shells)^2 - inner_length^2 <= max_tiles
    4 * num_shells^2 + 4 * inner_length * num_shells <= max_tiles
    num_shells^2 + inner_length * num_shells - max_shells / 4 <= 0
    num_shells <= (- inner_length + sqrt(inner_length^2 + max_shells)) / 2 (+ because num_shells >= 1)
    """
    count = 0
    inner_length = 1
    while (inner_length + 2)**2 - inner_length**2 <= max_tiles:
        num_shells = int((isqrt(inner_length**2 + max_tiles) - inner_length) / 2)
        count += num_shells
        inner_length += 1
    return count


print(get_num_hollow_sq_laminae(10**6))
