lvls = [[int(j) for j in i.strip().split()] for i in open('in.txt').readlines()]

def safe(l):
    l2 = sorted(l)
    lrev = sorted(l, reverse=True)
    if l != l2 and l != lrev:
        return False
    for i in range(len(l) - 1):
        diff = abs(l[i] - l[i+1])
        if diff < 1 or diff > 3:
            return False
            break
    return True 

ok = 0
for l in lvls:
    if safe(l):
        ok += 1
print(ok)

ok = 0
for l in lvls:
    if safe(l):
        ok += 1
    else:
        for j in range(len(l)):
            if safe(l[:j] + l[j+1:]):
                ok += 1
                print(l)
                break

print(ok)

