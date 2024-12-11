a = [int(i) for i in open('in.txt').read().strip().split()]


def step(l):
    ret = []
    for i in l:
        if i == 0:
            ret.append(1)
        elif len(str(i)) % 2 == 0:
            z = str(i)
            k = len(z) // 2
            ret.append(int(z[:k]))
            ret.append(int(z[k:]))
        else:
            ret.append(i * 2024)
    return ret

for i in range(25):
    a = step(a)
print(len(a))

a = [int(i) for i in open('in.txt').read().strip().split()]
memo = {}
def stepmemo(l, steps):
    if steps == 0:
        return 1
    ret = 0
    if (l, steps) in memo:
        return memo[(l, steps)]
    if l == 0:
        ret += stepmemo(1, steps - 1)
    elif len(str(l)) % 2 == 0:
        z = str(l)
        k = len(z) // 2
        ret += stepmemo(int(z[:k]), steps - 1)
        ret += stepmemo(int(z[k:]), steps - 1)
    else:
        ret += stepmemo(l * 2024, steps - 1)
    memo[(l, steps)] = ret
    return ret


ctr = 0
for i in a:
    ctr += stepmemo(i, 75)
print(ctr)
