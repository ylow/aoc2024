import regex as re
a = open('in.txt').read().strip()
z = 0
for i in re.findall('mul\((\d+),(\d+)\)',a):
    z += int(i[0])*int(i[1])
print(z)

z = 0
ok = True
for i in re.findall('((mul)\((\d+),(\d+)\))|(do\(\))|(don\'t\(\))',a):
    if len(i[4]) > 0:
        ok = True
    elif len(i[5]) > 0:
        ok = False 
    elif len(i[0]) > 0:
        if ok:
            z += int(i[2])*int(i[3])
print(z)
