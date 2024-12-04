a = open('in.txt').readlines()

s = 'XMAS'
def xmas(a, i, j, di, dj, p):
    if a[i][j] == s[p]:
        if p == len(s) - 1:
            return 1
        if 0 <= i + di < len(a) and 0 <= j + dj < len(a[0]):
            return xmas(a, i + di, j + dj, di, dj, p + 1)
    return 0

ctr = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)):
            ctr += xmas(a, i, j, di, dj, 0)
print(ctr)


def xmas2(a, i, j, p):
    if a[i][j] != 'A':
        return 0
    q,r,s,t= a[i-1][j-1], a[i-1][j+1], a[i+1][j+1], a[i+1][j-1]
    for _ in range(4):
        if q == r == 'M' and s == t == 'S':
            return 1
        q,r,s,t = r,s,t,q
    return 0

ctr = 0
for i in range(1, len(a) - 1):
    for j in range(1, len(a[0])-1):
        ctr += xmas2(a, i, j, 0)
print(ctr)
