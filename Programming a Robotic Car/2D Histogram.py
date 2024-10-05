colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['red', 'green', 'red' ,'green', 'red']
motions = [[0,0],[0,1],[0,1],[1,0],[1,0]]
sensor_right = 0.7
p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

p = []
y = len(colors)
x = len(colors[0])
n = x*y
for i in range(y):
    p.append([])
    for j in range(x):
        p[i].append(1./n)
        
def normalize (p):
    n=0
    q=[]
    for i in range(y):
        for j in range(x):
            n = n + p[i][j]
    for i in range(y):
        q.append([])
        for j in range(x):
            q[i].append(p[i][j]/n)
    return q

def move (p, move):
    q=[]
    for i in range(y):
        q.append([])
        for j in range(x):
            q[i].append(p[(i-move[0])%y][(j-move[1])%x]*p_move+p[i][j]*(1-p_move))
    return q
    
def sense (p, measure):
    q=[]
    for i in range(y):
        q.append([])
        for j in range(x):
            match = (measure == colors[i][j])
            q[i].append(p[i][j]*(sensor_right*match+(1-match)*(1-sensor_right)))
    return q
        
for i in range(len(motions)):
    p = move(p, motions[i])
    p = sense(p, measurements[i])

p = normalize(p)
show(p)
