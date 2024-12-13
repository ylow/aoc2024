import re
import numpy as np
ACOST = 3
BCOST = 1
C =10000000000000


def lsolve(ax,ay,bx,by,px,py):
    # solving the linear system
    # ca * ax + cb * bx = px
    # ca * ay + cb * by = py
    X = np.array([[ax,bx],[ay,by]])
    y = np.array([px,py])
    r = np.linalg.solve(X,y)
    ca = int(round(r[0],0))
    cb = int(round(r[1],2))
    if ca * ax + cb * bx == px and ca * ay + cb * by == py:
        return ACOST * ca + BCOST * cb
    return None



f = [a.strip() for a in open('in.txt').readlines() if len(a.strip()) > 0]
total = 0
for i in range(0, len(f), 3):
    baline = f[i]
    bbline = f[i+1]
    pline = f[i+2]
    assert(pline[:5] == 'Prize')
    bamatch = re.match('Button A: X\+([0-9]+), Y\+([0-9]+)', baline)
    bbmatch = re.match('Button B: X\+([0-9]+), Y\+([0-9]+)', bbline)
    pmatch = re.match('Prize: X\=([0-9]+), Y\=([0-9]+)', pline)
    ax = int(bamatch.group(1))
    ay = int(bamatch.group(2))
    bx = int(bbmatch.group(1))
    by = int(bbmatch.group(2))
    px = C + int(pmatch.group(1))
    py = C + int(pmatch.group(2))
    print(ax,ay)
    print(bx,by)
    print(px,py)
    r = lsolve(ax,ay,bx,by,px,py)
    if r is not None:
        print("OK", r)
        total += r 
print(total)
