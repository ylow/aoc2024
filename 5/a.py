order = [[int(i) for i in a.strip().split('|')] for a in open('in1.txt').readlines()]
upd = [[int(i) for i in a.strip().split(',')] for a in open('in2.txt').readlines()]

s = 0
for row in upd:
    pageorder = {}
    for i,j in enumerate(row):
        pageorder[j] = i
    valid = True
    for i,j in order:
        if i in pageorder and j in pageorder:
            if pageorder[i] > pageorder[j]:
                valid = False
                break
    if valid:
        s += row[int(len(row) / 2)]
print(s)



s = 0
for row in upd:
    pageorder = {}
    for i,j in enumerate(row):
        pageorder[j] = i
    valid = True
    for i,j in order:
        if i in pageorder and j in pageorder:
            if pageorder[i] > pageorder[j]:
                valid = False
                break
    if not valid:
        # reorder
        changes = True
        while changes:
            changes = False
            for i,j in order:
                if i in pageorder and j in pageorder:
                    if pageorder[i] > pageorder[j]:
                        pageorder[i], pageorder[j] = pageorder[j], pageorder[i]
                        changes = True
        idx = int(len(row) / 2)
        for k,v in pageorder.items():
            if v == idx:
                s += k
                break
print(s)
