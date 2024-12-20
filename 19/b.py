f = open('in.txt', 'r').readlines()
towels = [x.strip() for x in f[0].strip().split(',')]
f = [x.strip() for x in f[2:]]

print(towels)
memo = {}
def solve(r, towels):
    if len(r) == 0:
        return 1
    if r in memo:
        return memo[r]
    ctr = 0
    for t in towels:
        if r.startswith(t):
            ret = solve(r[len(t):], towels)
            memo[r[len(t):]] = ret
            ctr += ret
    memo[r] = ctr
    return ctr

ctr = 0
z = 0
for i in f:
    ctr += solve(i, towels)
    z += 1
    print(z, len(f))
print(ctr)



