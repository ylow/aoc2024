import copy
a = list(open('in.txt').read().strip())
d = []
ctr = 0
free = False
for i in a:
    l = int(i)
    if not free:
        d.append([ctr, l])
        ctr += 1
    else:
        d.append([-1, l])
    free = not free
dclone = copy.deepcopy(d)

lastfno = ctr - 1
#print(d)
# defrag
c = 0
while c < len(d):
    # remove free space at end
    while d[len(d) - 1][0] == -1:
        d.pop()
    if d[c][0] == -1:
        last = len(d) - 1
        shiftlen = min(d[c][1], d[last][1])
        if shiftlen == 0:
            c += 1
            continue
        d[c][1] -= shiftlen
        d[last][1] -= shiftlen
        flen = d[last][1]
        d.insert(c, [d[last][0], shiftlen])
        # if last is empty remove
        if flen == 0:
            d.pop()
    else:
        c += 1
#print(d)

def score(d):
    ctr = 0
    s = 0
    for f,l in d:
        if f == -1:
            ctr += l
            continue
        for i in range(l):
            s += ctr * f
            ctr += 1
    print(s)

score(d)
d = dclone
for f in range(lastfno, -1, -1):
    # find f
    pos = -1
    for i in range(len(d)):
        if d[i][0] == f:
            pos = i
            break
    flen = d[pos][1]
    assert(pos >= 0)
    for i in range(pos):
        if d[i][0] == -1 and d[i][1] >= flen:
            # shift to fit
            shiftlen = flen
            if shiftlen == d[i][1]:
                d[i][0] = f
                d[pos][0] = -1
            else:
                d[pos][0] = -1
                d[i][1] -= shiftlen
                d.insert(i, [f, flen])
            break
score(d)
