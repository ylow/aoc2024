a = []
b = []
for i in open('in1.txt').readlines():
    z=i.strip().split(' ')
    a.append(int(z[0]))
    b.append(int(z[len(z)-1]))
a.sort()
b.sort()
t = 0
for i,j in zip(a,b):
    t += abs(i-j)
print(t)

t = 0
for i in a:
    t += i * len([j for j in b if j==i])

print(t)
