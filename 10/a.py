a = [[int(i) for i in s.strip()] for s in open('in.txt').readlines()]

def dfs(x, y, v):
    if 0 <= x < len(a) and 0 <= y < len(a[0]):
        if a[x][y] == v:
            if v == 9:
                return [(x,y)]
            return dfs(x+1,y,v+1) + dfs(x-1,y,v+1) + dfs(x,y-1,v+1) + dfs(x,y+1,v+1)
        else:
            return []
    else:
        return []

s = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == 0:
            s += len(set(dfs(i,j,0)))
print(s)

s = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == 0:
            s += len(dfs(i,j,0))
print(s)
