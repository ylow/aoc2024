import copy
import re
f = [a.strip() for a in open('in.txt').readlines() if len(a.strip()) > 0]
robots = []
for i in range(0, len(f)):
    m = re.findall('([0-9\-]+)', f[i])
    robots.append([int(j) for j in m])

print(robots)

WIDTH = 101
HEIGHT = 103
STEPS = 100
poses = []

WHALF = WIDTH // 2
HHALF = HEIGHT // 2
quadrant = [[0,0],[0,0]]
for p1,p2,v1,v2 in robots:
    x = (p1 + v1 * STEPS) % WIDTH
    y = (p2 + v2 * STEPS) % HEIGHT
    if x == WHALF or y == HHALF:
        continue
    quadrant[x > WHALF][y > HHALF] += 1

print(quadrant)
print(quadrant[0][0] * quadrant[0][1] * quadrant[1][0] * quadrant[1][1])

def print_robots(r):
    for i in range(HEIGHT):
        s = ''
        for j in range(WIDTH):
            if r[i][j] == 0:
                s += '.'
            else:
                s += 'X'
        print(s)

h = {}
for i in range(11000):
    quadrant = [[0,0],[0,0]]
    skips = 0
    r = [[0] * WIDTH for _ in range(HEIGHT)]
    for p1,p2,v1,v2 in robots:
        x = (p1 + v1 * i) % WIDTH
        y = (p2 + v2 * i) % HEIGHT
        r[y][x] += 1
        if x == WHALF or y == HHALF:
            skips += 1
            continue
        quadrant[x > WHALF][y > HHALF] += 1
    #n = sum(r)
    #if n[45] > 30 and n[1] == 0 and n[100] == 0:
    z= str(r)
    if z not in h:
        h[z] = r
    else:
        print("CYCLE ", i)
        break
    if i % 101 == 14:
        print(i, quadrant, skips)
        print_robots(r)
