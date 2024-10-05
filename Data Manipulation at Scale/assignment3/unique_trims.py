import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: sequence id
    # value: sequence
    value = record[1][:-10]
    mr.emit_intermediate(value, None)

def reducer(key, list_of_values):
    # key: trimmed sequence
    # value: None
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
