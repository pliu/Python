def simple_linear_regression(input_feature, output):
    sum_input = 0
    sum_output = 0
    sum_input_output = 0
    sum_input_squared = 0
    for i in xrange(len(input_feature)):
        sum_input += input_feature[i]
        sum_output += output[i]
        sum_input_output += input_feature[i]*output[i]
        sum_input_squared += input_feature[i]**2

    return closedForm(len(input_feature), sum_input, sum_output, sum_input_output, sum_input_squared)

def closedForm(n, sum_input, sum_output, sum_input_output, sum_input_squared):
    slope = (sum_input_output - sum_input*sum_output/n)/(sum_input_squared - sum_input**2/n)
    intercept = sum_output/n - slope*sum_input/n
    return (intercept, slope)

def get_residual_sum_of_squares(input_feature, output, intercept, slope):
    RSS = 0
    for i in xrange(len(input_feature)):
        RSS += (output[i] - input_feature[i]*slope - intercept)**2
    return RSS

def inverse_regression_predictions(output, intercept, slope):
    return (output - intercept)/slope

def getData(file_path, input_name, output_name):
    file = open(file_path)
    line = file.readline()
    tokens = line.split(",")
    input = tokens.index(input_name)
    output = tokens.index(output_name)
    input_data = []
    output_data = []
    while (file):
        line = file.readline()
        tokens = line.split(",")
        if len(tokens) == 1:
            break
        input_data.append(float(tokens[input]))
        output_data.append(float(tokens[output]))

    return(input_data, output_data)

data = getData("D:\Work\Programming\Python\Regression\kc_house_train_data.csv", "sqft_living", "price")
params = simple_linear_regression(data[0], data[1])
print params[0], params[1]
print 2650*params[1] + params[0]
print get_residual_sum_of_squares(data[0], data[1], params[0], params[1])
print inverse_regression_predictions(800000, params[0], params[1])
data = getData("D:\Work\Programming\Python\Regression\kc_house_test_data.csv", "sqft_living", "price")
print get_residual_sum_of_squares(data[0], data[1], params[0], params[1])