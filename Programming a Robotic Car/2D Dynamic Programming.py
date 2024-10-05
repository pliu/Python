grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]

goal = [0, len(grid[0])-1] # Goal is in top right corner


delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

success_prob = 0.5
failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
collision_cost = 100
cost_step = 1
                     

def direction_cost(value, i, j, direction):
    cost = cost_step
    if i+delta[direction][0] < 0 or j+delta[direction][1] < 0 or i+delta[direction][0] >= len(grid) or j+delta[direction][1] >= len(grid[i]):
        cost += success_prob * collision_cost
    else:
        cost += success_prob * value[i+delta[direction][0]][j+delta[direction][1]]
    if i+delta[(direction-1)%4][0] < 0 or j+delta[(direction-1)%4][1] < 0 or i+delta[(direction-1)%4][0] >= len(grid) or j+delta[(direction-1)%4][1] >= len(grid[i]):
        cost += failure_prob * collision_cost
    else:
        cost += failure_prob * value[i+delta[(direction-1)%4][0]][j+delta[(direction-1)%4][1]]
    if i+delta[(direction+1)%4][0] < 0 or j+delta[(direction+1)%4][1] < 0 or i+delta[(direction+1)%4][0] >= len(grid) or j+delta[(direction+1)%4][1] >= len(grid[i]):
        cost += failure_prob * collision_cost
    else:
        cost += failure_prob * value[i+delta[(direction+1)%4][0]][j+delta[(direction+1)%4][1]]
    return cost

def find_min(value, i, j, policy):
    min_cost = collision_cost*10
    for k in range (len (delta)):
        temp_cost = direction_cost(value, i , j, k)
        if temp_cost < min_cost:
            min_cost = temp_cost
            min_index = k
    if min_cost < value[i][j]:
        policy[i][j] = delta_name[min_index]
        return min_cost
    return value[i][j]

def stochastic_value():
    value = [[collision_cost for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    value[goal[0]][goal[1]] = 0
    delta_value = 1
    while delta_value > 0.00001:
        delta_value = 0
        for i in range (len(grid)):
            for j in range (len(grid[i])):
                if grid[i][j] != 1 and ([i, j] != goal):
                    temp_value = find_min(value, i, j, policy)
                    if abs(temp_value - value[i][j]) > delta_value:
                        delta_value = abs(temp_value - value[i][j])
                    value[i][j] = temp_value
    for i in range (len(grid)):
        for j in range (len(grid[i])):
            if grid[i][j] == 1:
                value[i][j] = 1000
    policy[goal[0]][goal[1]] = '*'
    return value, policy
    
value, policy = stochastic_value()
for i in value:
    print i
for i in policy:
    print i