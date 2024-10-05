import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person A
    # value: person B
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)
    mr.emit_intermediate(value, key)

def reducer(key, list_of_values):
    # key: person A
    # value: person B
    asymmetric_friends = {}
    for friend in list_of_values:
        if friend not in asymmetric_friends:
            asymmetric_friends[friend] = 1
        else:
            asymmetric_friends.pop(friend)
    for friend in asymmetric_friends:
        mr.emit((key, friend))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
