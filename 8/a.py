a = [list(a.strip()) for a in open('in.txt').readlines()]

h = len(a)
w = len(a[0])
ants = {}
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] != '.':
            ant = a[i][j]
            if ant not in ants:
                ants[ant] = []
            ants[ant].append((i,j))

inrange = lambda x,y: 0 <= x < h and 0 <= y < w

ctr = set()
for ant, el in ants.items():
    for i in range(len(el)):
        for j in range(i+1, len(el)):
            (a,b) = el[i]
            (c,d) = el[j]
            dx,dy = c-a, d-b
            antix, antiy = a-dx, b-dy
            if inrange(antix, antiy):
                ctr.add((antix, antiy))
            antix, antiy = c+dx, d+dy
            if inrange(antix, antiy):
                ctr.add((antix, antiy))
print(len(ctr))

ctr = set()
for ant, el in ants.items():
    for i in range(len(el)):
        for j in range(i+1, len(el)):
            (a,b) = el[i]
            (c,d) = el[j]
            ctr.add((c,d))
            dx,dy = c-a, d-b
            antix, antiy = a, b
            while inrange(antix, antiy):
                ctr.add((antix, antiy))
                antix, antiy = antix-dx, antiy-dy

            antix, antiy = c, d
            while inrange(antix, antiy):
                ctr.add((antix, antiy))
                antix, antiy = antix+dx, antiy+dy
print(len(ctr))
