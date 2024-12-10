a = [x.split(':') for x in open('in.txt').readlines()]
for i in range(len(a)):
    a[i][0] = int(a[i][0])
    a[i][1] = [int(x) for x in a[i][1].strip().split(' ')]

def sols(nlist):
    if len(nlist) == 1:
        return [nlist[0]]
    r = nlist[len(nlist) - 1]
    s = sols(nlist[:len(nlist) - 1])
    s = [r * i for i in s] + [r + i for i in s]
    return s

f = 0
for res, l in a:
    if res in sols(l):
        f += res
print(f)


def sols2(nlist):
    if len(nlist) == 1:
        return [nlist[0]]
    r = nlist[len(nlist) - 1]
    s = sols2(nlist[:len(nlist) - 1])
    s = [i*r for i in s] + [i+r for i in s] + [int(str(i) + str(r)) for i in s]
    return s

f = 0
for res, l in a:
    if res in sols2(l):
        f += res
print(f)
