a = [list(s.strip()) for s in open('in.txt').readlines()]
mark = [[None]*len(a[0]) for _ in range(len(a))]


def count_ve(i, j, v):
    # count the number of "vertices" and "edges" in the connected component
    # starting from (i, j) with value v
    q = [(i, j)]
    e = set()
    mark[i][j] = v
    vertices = 0
    edges = 0
    while q:
        i, j = q.pop()
        vertices += 1
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < len(a) and 0 <= nj < len(a[0]) and a[ni][nj] == v:
                if mark[ni][nj] is None:
                    mark[ni][nj] = v
                    q.append((ni, nj))
                    e.add((min(i,ni), min(j,nj), max(i,ni),max(j,nj)))
                elif mark[ni][nj] == v:
                    e.add((min(i,ni), min(j,nj), max(i,ni),max(j,nj)))
    return vertices, len(e)

u = {}
for i in range(len(a)):
    for j in range(len(a[0])):
        if mark[i][j] is not None:
            continue
        v, e = count_ve(i, j, a[i][j])
        perim = 4*v-2*e
        if a[i][j] not in u:
            u[a[i][j]] = 0
        print(a[i][j], v, e, perim)
        u[a[i][j]] += v*perim

s = 0
for k, v in u.items():
    print(k, v)
    s += v
print(s)



def list_exterior_e(i, j, v):
    # count the number of "vertices" and "edges" in the connected component
    # starting from (i, j) with value v
    q = [(i, j)]
    e = set()
    alle = set()
    mark[i][j] = v
    vertices = 0
    edges = 0
    while q:
        i, j = q.pop()
        vertices += 1
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i+di, j+dj
            alle.add((i, j, ni, nj))
            if 0 <= ni < len(a) and 0 <= nj < len(a[0]) and a[ni][nj] == v:
                if mark[ni][nj] is None:
                    mark[ni][nj] = v
                    q.append((ni, nj))
                    e.add((i, j, ni, nj))
                    e.add((ni, nj, i, j))
                elif mark[ni][nj] == v:
                    e.add((i, j, ni, nj))
                    e.add((ni, nj, i, j))
    return vertices, alle.difference(e)

mark = [[None]*len(a[0]) for _ in range(len(a))]

def same(e1, e2):
    # vertical edge
    if e1[1] == e1[3]:
        # also vertical edge
        # and same row
        # and one shifted
        return e2[1] == e2[3] and  \
               e1[0] == e2[0] and \
               e1[2] == e2[2] and \
               abs(e2[1] - e1[1]) == 1
    elif e1[0] == e1[2]:
        return e2[0] == e2[2] and \
               e1[1] == e2[1] and \
               e1[3] == e2[3] and \
               abs(e2[0] - e1[0]) == 1 
    return False

def ugly_union(uf, e1,e2):
    if uf[e1] != uf[e2]:
        src = uf[e2]
        targ = uf[e1]
        for k in uf.keys():
            if uf[k] == src:
                uf[k] = targ
def count_cont_edges(e):
    uf = {}
    for i in range(len(e)):
        uf[e[i]] = i
    # quick and dirty disjoint set
    for i in range(len(e)):
        for j in range(i+1, len(e)):
            if same(e[i], e[j]):
                ugly_union(uf, e[i], e[j])
    print(uf)
    return len(set(uf.values()))




total = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        if mark[i][j] is not None:
            continue
        vertices, exe = list_exterior_e(i, j, a[i][j])
        ce = count_cont_edges(list(exe))
        print(vertices, ce, a[i][j])
        total += vertices * ce
print(total)
