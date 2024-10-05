###########################
# 6.00.2x Problem Set 1: Space Cows

from pset1.ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


class Node:
    def __init__(self, prev, nextn, value):
        self.prev = prev
        self.next = nextn
        self.value = value


class TraversableLinkedList:
    def __init__(self):
        self.virtual_start = Node(None, None, None)
        self.virtual_end = Node(self.virtual_start, None, None)
        self.virtual_start.next = self.virtual_end
        self.current = self.virtual_start

    def add_left(self, value):
        prev_first = self.virtual_start.next
        new_node = Node(self.virtual_start, prev_first, value)
        self.virtual_start.next = new_node
        prev_first.prev = new_node

    def add_right(self, value):
        prev_last = self.virtual_end.prev
        new_node = Node(prev_last, self.virtual_end, value)
        self.virtual_end.prev = new_node
        prev_last.next = new_node

    def start_traversal(self):
        self.current = self.virtual_start

    def next(self):
        if self.current.next is not self.virtual_end:
            self.current = self.current.next
            return self.current.value

    def is_empty(self):
        return self.virtual_start.next is self.virtual_end

    def remove_current(self):
        prev = self.current.prev
        nextn = self.current.next
        prev.next = nextn
        nextn.prev = prev
        self.current = prev

    def __repr__(self):
        current = self.virtual_start
        output = []
        while current.next is not self.virtual_end:
            current = current.next
            output.append(str(current.value))
        return ", ".join(output)


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    sorted_cows = sorted([{"weight": weight, "name": name} for name, weight in cows.items()], reverse=True, key=lambda x: x["weight"])
    tld = TraversableLinkedList()
    for d in sorted_cows:
        tld.add_right(d)
    result = []
    while not tld.is_empty():
        remaining_limit = limit
        current_passengers = []
        tld.start_traversal()
        while remaining_limit > 0:
            check = tld.next()
            if not check:
                break
            if check["weight"] <= remaining_limit:
                remaining_limit -= check["weight"]
                current_passengers.append(check["name"])
                tld.remove_current()
        result.append(current_passengers)
    return result


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cow_array = [(name, weight) for name, weight in cows.items()]
    least_rides = None
    least_partition = None
    for partition in get_partitions(cow_array):
        if least_rides is not None and len(partition) >= least_rides:
            continue
        valid = True
        for s in partition:
            if sum([o[1] for o in s]) > limit:
                valid = False
                break
        if valid:
            least_rides = len(partition)
            least_partition = partition
    result = []
    for s in least_partition:
        result.append([o[0] for o in s])
    return result


# Problem 3
def compare_cow_transport_algorithms(cows):
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
    greedy_cow_transport(cows)
    print(time.time() - start)
    start = time.time()
    brute_force_cow_transport(cows)
    print(time.time() - start)


"""
Here is some test data for you to see the results of your algorithms with.
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))
compare_cow_transport_algorithms(cows)


