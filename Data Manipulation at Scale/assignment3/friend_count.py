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

def reducer(key, list_of_values):
    # key: person A
    # value: person B
    mr.emit((key, len(list_of_values)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
