import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order_id
    # value: record (record[0] is which table the record is from)
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: order_id
    # value: record
    list_of_line_items = []
    list_of_orders = []
    for v in list_of_values:
        if v[0] == 'line_item':
            list_of_line_items.append(v)
        elif v[0] == 'order':
            list_of_orders.append(v)
    for o in list_of_orders:
        for l in list_of_line_items:
            mr.emit(o + l)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
