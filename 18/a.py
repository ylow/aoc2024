import queue
LIMIT = 1024 
GRID_SIZE = 71
grid = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
costs = [[1000000 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
locs = [[int(i) for i in a.strip().split(',')] for a in open('in.txt').readlines()]

#LIMIT=12
#GRID_SIZE=7
for i in range(LIMIT):
    grid[locs[i][0]][locs[i][1]] = 1

def heuristic(i,j):
    return GRID_SIZE - i + GRID_SIZE - j

DIRS = [(0,1),(1,0),(0,-1),(-1,0)]


def astar(i,j,grid, costs):
    pq = queue.PriorityQueue()
    pq.put((heuristic(i,j),(i,j, 0)), False)
    while not pq.empty():
        _,(i,j, c) = pq.get(False)
        if (i == GRID_SIZE-1) and (j == GRID_SIZE-1):
            print(c)
        # visited
        if costs[i][j] <= c:
            continue
        costs[i][j] = c
        for di, dj in DIRS:
            ni,nj = i + di, j + dj
            nc = c + 1
            if ni < 0 or nj < 0 or ni >= GRID_SIZE or nj >= GRID_SIZE or grid[ni][nj]:
                continue
            if costs[ni][nj] > nc:
                pq.put((nc + heuristic(ni,nj),(ni,nj, nc)), False)

astar(0,0,grid, costs)
print(costs[GRID_SIZE-1][GRID_SIZE-1])


def test_limit(k):
    grid = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    costs = [[1000000 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for i in range(k):
        grid[locs[i][0]][locs[i][1]] = 1
    astar(0,0,grid,costs)
    return costs[GRID_SIZE-1][GRID_SIZE-1] < 1000000

# dumb binary search
# low is always admissible
# high is always not
low = 1024
high = 3450
while high > low + 1:
    mid = (low + high) // 2
    print(low,mid,high)
    if test_limit(mid):
        low = mid
    else:
        high = mid
print(locs[high-1])
