# Given an array of integers, return the number of quartets, x_i, x_j, x_k, x_l where i, j, k, and l are indices into
# the array, i < j < k < l, and x_i + x_j - x_k = x_l.

"""
Start by rearranging the x_i + x_j - x_k = x_l <=> x_i + x_j = x_k + x_l.

Construct pairwise sum maps for x_i and x_j and x_k and x_l where the key is the sum and the value is a list of tuples
of the form (earlier index, later index) where earlier index < later index. The map for x_i/x_j is constructed such that
the list of tuples for any given key is weakly monotonically increasing by j. The map for x_k/x_l is constructed such
that the list of tuples for any given key is weakly monotonically increasing by k.

For every key in the x_i/x_j map, if there is a corresponding key in the x_k/x_l map, then we have found possible
quartets, x_i, x_j, x_k, and x_l, such that x_i + x_j = x_k + x_l.

To satisfy the condition that i < j < k < l, we make use of the way we previously constructed our maps. Within each map,
we are guaranteed that i < j and k < l, thus, so long as j < k, we have discovered a valid quartet. As the tuples in the
x_i/x_j map are weakly monotonically increasing by j and the tuples in the x_k/x_l map are weakly monotonically
increasing by k, we use a merge sort-like procedure to find all of the valid x_k/x_l pairs for the x_i/x_j pairs.
"""

from collections import defaultdict


def num_ordered_quartet_sum_zero(array):
    i_j_map = defaultdict(list)
    k_l_map = defaultdict(list)

    for x in xrange(1, len(array)):
        for y in xrange(x):
            i_j_map[array[x] + array[y]].append((y, x))

    for x in xrange(len(array) - 1):
        for y in xrange(x + 1, len(array)):
            k_l_map[array[x] + array[y]].append((x, y))

    count = 0
    for key, i_j_pairs in i_j_map.items():
        if key not in k_l_map:
            continue
        k_l_pairs = k_l_map[key]
        index = 0
        for i_j_pair in i_j_pairs:
            j = i_j_pair[1]
            while index < len(k_l_pairs) and k_l_pairs[index][0] <= j:
                index += 1
            # modify here if we want to return back the exact quartets that satisfy the condition and not only the count
            count += len(k_l_pairs) - index

    return count


print(num_ordered_quartet_sum_zero([1, 1, 2, 3, 3, 3, 3, 0, 0]))
