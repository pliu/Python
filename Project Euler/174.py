# https://projecteuler.net/problem=174

from collections import defaultdict


def get_num_formable_sq_laminae(max_tiles):
    """
    Returns a map of the number of sq laminae that can be formed with t tiles for t <= max_tiles
    Method:
    The max outer_length of the square is floor((max_tiles + 4)/4)
    The min outer_length of a square that has an inner, empty square, is 3
    For every outer_length, the number of tiles used for every size of inner square is given by outer_length^2 - inner_length^2
    The inner_length must be an even length different from the outer_length to ensure that the thickness of tiles is uniform
    Optimization:
    We precompute the squares from 0 - the max outer_length
    """
    formable_count = defaultdict(lambda: 0)
    outer_length = int((max_tiles + 4)/4)
    squares = [i**2 for i in range(outer_length + 1)]
    while outer_length >= 3:
        inner_length = outer_length - 2
        tiles_used = squares[outer_length] - squares[inner_length]
        while inner_length >= 1 and tiles_used <= max_tiles:
            formable_count[tiles_used] += 1
            inner_length -= 2
            tiles_used = squares[outer_length] - squares[inner_length]
        outer_length -= 1
    return formable_count


def get_filtered_num_formable_sq_lamina(max_tiles, max_formable):
    formable_count = get_num_formable_sq_laminae(max_tiles)
    count = 0
    for value in formable_count.values():
        if 1 <= value <= max_formable:
            count += 1
    return count


print(get_filtered_num_formable_sq_lamina(10**6, 10))
