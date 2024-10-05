import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: (i, j) where i is fixed if the entry is from matrix a and j is fixed if the entry is from
    #      matrix b
    # value: entry (matrix, i, j, value)
    rows_a = 5
    cols_b = 5
    if record[0] == 'a':
        for j in xrange(cols_b):
            mr.emit_intermediate((record[1], j), record)
    else:
        for i in xrange(rows_a):
            mr.emit_intermediate((i, record[2]), record)

def reducer(key, list_of_values):
    # key: (i, j) coordinate of result matrix
    # value: entry
    sum = 0
    col_a = {}
    b = []
    for entry in list_of_values:
        if entry[0] == 'a':
            col_a[entry[2]] = entry
        else:
            b.append(entry)
    for entry in b:
        if entry[1] in col_a:
            sum += entry[3]*col_a[entry[1]][3]
    mr.emit((key[0], key[1], sum))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
