a = [int(i) for i in open('in.txt').read().strip().split()]


def stone_generator(stone, step):
    if step == 0:
        yield stone
    elif stone == 0:
        yield from stone_generator(1, step - 1)
    elif len(str(stone)) % 2 == 0:
        z = str(stone)
        k = len(z) // 2
        yield from stone_generator(int(z[:k]), step - 1)
        yield from stone_generator(int(z[k:]), step - 1)
    else:
        yield from stone_generator(stone * 2024, step - 1)


def generate_all(stonelist, step):
    for i in stonelist:
        yield from stone_generator(i, step)


nsteps = 30
ctr = 0
for i in generate_all(a, nsteps):
    ctr += 1
print(ctr)
