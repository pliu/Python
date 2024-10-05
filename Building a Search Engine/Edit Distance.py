import heapq

def edit_distance(s,t):
    def generate_heuristic(s,t):
        heuristic = []
        for i in range(len(s)+1):
            heuristic.append([])
            for j in range(len(t)+1):
                heuristic[i].append(0)
        for i in range(len(s)):
            j = len(s) - i - 1
            k = len(t)
            while j >= 0 and k >= 0:
                heuristic[j][k] = i + 1
                j -= 1
                k -= 1
        for i in range(len(t)):
            j = len(t) - i - 1
            k = len(s)
            while j >= 0 and k >= 0:
                heuristic[k][j] = i + 1
                j -= 1
                k -= 1
        return heuristic
                
    def find_path (path, expand, location):
        path[goal[0]][goal[1]] ='*'
        while location != init:
            min = 0
            for i in range(len(delta)):
                y = location[0]-delta[i][0]
                x = location[1]-delta[i][1]
                if y>=0 and y<len(s)+1 and x>=0 and x<len(t)+1 and expand[y][x]!=-1:
                    if expand[location[0]][location[1]]-expand[y][x]>min:
                        min = expand[location[0]][location[1]]-expand[y][x]
                        move = i
            location[0] = location[0]-delta[move][0]
            location[1] = location[1]-delta[move][1]
            path[location[0]][location[1]] = delta_name[move]
    
    def search(s,t):
        path = [[' ' for row in range(len(t)+1)] for col in range(len(s)+1)]
        expand = [[-1 for row in range(len(t)+1)] for col in range(len(s)+1)]
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
                    find_path (path, expand, element[1])
                    for i in path:
                        print i
                    return element[0]#+heuristic[element[1][0]][element[1][1]]
                    #When using heuristics, this (^) extra term needs to be added to the final cost.
                    #Moreover, element[1] must first be mutated within find_path before the correct edit
                    #distance is achieved. Lastly, either way, the path that is found is incorrect.
                visited.append(element[1])
                for i in range(len(delta)):
                    y = element[1][0] + delta[i][0]
                    x = element[1][1] + delta[i][1]
                    if y>=0 and y<len(s)+1 and x>=0 and x<len(t)+1:
                        check = [y, x]
                        temp_cost = element[0]+cost#+heuristic[y][x]-heuristic[element[1][0]][element[1][1]]
                        if i == 0 and s[y-1] == t[x-1]:
                            temp_cost -= cost
                        heapq.heappush(border, (temp_cost,check))
    
    init = [0, 0]
    goal = [len(s), len(t)]
    delta = [[ 1, 1 ], # go diagonal
             [ 1, 0 ], # go down
             [ 0, 1 ]] # go right
    delta_name = ['D', 'v', '>']
    cost = 1
    #heuristic = generate_heuristic(s,t)
    return search(s,t)


print edit_distance ("peng liu","joanne lee")

