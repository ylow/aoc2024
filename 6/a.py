a = [list(x.strip()) for x in open('in.txt').readlines()]

def inbounds(gi, gj):
    return 0 <= gi < len(a) and 0 <= gj < len(a[0])

gpos = []

for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == '^':
            gi = i
            gj = j
initialgi = gi
initialgj = gj

dirs = [(-1, 0), (0,1), (1,0), (0,-1)]
gd = 0

gpos = set([(gi, gj)])

ctr = 0
while True:
    tgi = gi + dirs[gd][0]
    tgj = gj + dirs[gd][1]
    if not inbounds(tgi, tgj):
        break
    if a[tgi][tgj] == '#':
        gd = (gd + 1) % 4
        continue
    gi, gj = tgi, tgj
    gpos.add((gi, gj))

print(len(gpos))


# B
# reset

def inloop():
    gd = 0
    gi, gj = initialgi, initialgj
    gpos = set([(gi, gj, gd)])
    while True:
        tgi = gi + dirs[gd][0]
        tgj = gj + dirs[gd][1]
        if not inbounds(tgi, tgj):
            break
        if a[tgi][tgj] == '#':
            gd = (gd + 1) % 4
            continue
        gi, gj = tgi, tgj
        if (gi, gj, gd) in gpos:
            return True 
        gpos.add((gi, gj, gd))
    return False

ctr = 0
for i in range(len(a)):
    print(i, len(a))
    for j in range(len(a[0])):
        if a[i][j] == '.':
            a[i][j] = '#'
            if inloop():
                ctr += 1
            a[i][j] = '.'
print(ctr)
