import re
ACOST = 3
BCOST = 1


def insert_if_cheaper(d,x,y,ca,cb,cost, i):
    if (x,y) in d:
        _,_,oldcost = d[(x,y)]
        if cost >= oldcost:
            return False
    d[(x,y)] = (ca,cb,cost)
    return True

def dpsolve(ax,ay,bx,by,tx,ty):
    d = {(ax,ay):(1,0,ACOST),
         (bx,by):(0,1,BCOST)}
    i = 0
    while True:
        i += 1
        changed = False
        for (x,y),(ca,cb,cost) in list(d.items()): 
            if ca + cb != i:
                continue
            if ca >= 100 or cb >= 100:
                continue
            if insert_if_cheaper(d,x+ax,y+ay,ca+1,cb,cost+ACOST, i):
                changed = True
            if insert_if_cheaper(d,x+bx,y+by,ca,cb+1,cost+BCOST, i):
                changed = True
        if changed is False:
            break
    if (tx,ty) in d:
        return d[(tx,ty)][2]
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
    px = int(pmatch.group(1))
    py = int(pmatch.group(2))
    print(ax,ay)
    print(bx,by)
    print(px,py)
    r = dpsolve(ax,ay,bx,by,px,py)
    if r is not None:
        total += r 
print(total)
