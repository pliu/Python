import heapq

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

heuristic = [[9, 8, 7, 6, 5, 4],
            [8, 7, 6, 5, 4, 3],
            [7, 6, 5, 4, 3, 2],
            [6, 5, 4, 3, 2, 1],
            [5, 4, 3, 2, 1, 0]]
            
#heuristic = [[0,0,0,0,0,0],
#             [0,0,0,0,0,0],
#             [0,0,0,0,0,0],
#             [0,0,0,0,0,0],
#             [0,0,0,0,0,0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def find_path (path, expand, location):
    path[goal[0]][goal[1]] ='*'
    while location != init:
        min = 0
        for i in range(len(delta)):
            y = location[0]-delta[i][0]
            x = location[1]-delta[i][1]
            if y>=0 and y<len(grid) and x>=0 and x<len(grid[0]) and expand[y][x]!=-1:
                if expand[location[0]][location[1]]-expand[y][x]>min:
                    min = expand[location[0]][location[1]]-expand[y][x]
                    move = i
        location[0] = location[0]-delta[move][0]
        location[1] = location[1]-delta[move][1]
        path[location[0]][location[1]] = delta_name[move]

def search():
    path = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    count = 0
    visited = []
    border = []
    heapq.heappush(border, (0,init))
    while border:
        element = heapq.heappop(border)
        if element[1] not in visited:
            expand[element[1][0]][element[1][1]] = count
            count += 1
            if element[1] == goal:
                print "Path found"
                for i in expand:
                    print i
                find_path (path, expand, element[1])
                for i in path:
                    print i
                return ""
            visited.append(element[1])
            for i in range(len(delta)):
                y = element[1][0] + delta[i][0]
                x = element[1][1] + delta[i][1]
                if y>=0 and y<len(grid) and x>=0 and x<len(grid[0]) and grid[y][x]!=1:
                    check = [y, x]
                    heapq.heappush(border,(element[0]+heuristic[y][x]-heuristic[element[1][0]][element[1][1]]+cost,check))
    return "No path"# make sure you return the shortest path.

print search()



