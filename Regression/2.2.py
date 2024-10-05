import numpy as np

def getData(file_path, input_names, output_names):
    file = open(file_path)
    line = file.readline()
    tokens = line.split(",")
    input_data = []
    output_data = []
    input_indices = []
    output_indices = []
    for input_name in input_names:
        input_indices.append(tokens.index(input_name))
        input_data.append([])
    for output_name in output_names:
        output_indices.append(tokens.index(output_name))
        output_data.append([])

    while (file):
        line = file.readline()
        tokens = line.split(",")
        if len(tokens) == 1:
            break
        for i in xrange(len(input_indices)):
            input_data[i].append(tokens[input_indices[i]])
        for i in xrange(len(output_indices)):
            output_data[i].append(tokens[output_indices[i]])

    return input_data, output_data

input, output = getData("kc_house_train_data.csv", ["sqft_living"], ["price"])
