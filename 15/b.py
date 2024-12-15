remap = {'#':'##', '.':'..', '@':'@.','O':'[]'}
board = [list(''.join(remap[c] for c in r.strip())) for r in open('in_board.txt').readlines()]
moves = open('in_moves.txt').read()

for i in range(len(board)):
    print(''.join(board[i]))


def try_shift(i,j,di,dj):
    ti,tj = i+di,j+dj
    if board[ti][tj] == '#':
        return False
    elif board[ti][tj] == '.':
        return True
    elif board[ti][tj] == '[':
        if di != 0:
            # shifting updown
            if try_shift(ti,tj,di,dj) and try_shift(ti,tj+1,di,dj):
                return True
        else:
            return try_shift(ti,tj,di,dj)
    elif board[ti][tj] == ']':
        if di != 0:
            # shifting updown
            if try_shift(ti,tj-1,di,dj) and try_shift(ti,tj,di,dj):
                return True
        else:
            return try_shift(ti,tj,di,dj)
    return False

def shift(i,j,di,dj):
    ti,tj = i+di,j+dj
    if board[ti][tj] == '#':
        return False
    elif board[ti][tj] == '.':
        board[ti][tj] = board[i][j]
        board[i][j] = '.'
        return True
    elif board[ti][tj] == '[':
        print(i,j,ti,tj)
        # can the whole box move
        if try_shift(ti,tj,di,dj) and try_shift(ti,tj+1,di,dj):
            if di != 0:
                # up down
                shift(ti,tj,di,dj)
                shift(ti,tj+1,di,dj)
            else:
                shift(ti,tj,di,dj)
            # move myself
            board[ti][tj] = board[i][j]
            board[i][j] = '.'
            return True
    elif board[ti][tj] == ']':
        # can the whole box move
        print(i,j,ti,tj)
        if try_shift(ti,tj-1,di,dj) and try_shift(ti,tj,di,dj):
            if di != 0:
                # up down
                shift(ti,tj-1,di,dj)
                shift(ti,tj,di,dj)
            else:
                shift(ti,tj,di,dj)
            # move myself
            board[ti][tj] = board[i][j]
            board[i][j] = '.'
            return True
    return False
    
directions = {'^':(-1,0), 'v':(1,0), '<':(0,-1), '>':(0,1)}


ri, rj = 0,0
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == '@':
            ri,rj = i,j
            
for i in moves:
    if i not in directions:
        continue
    di, dj = directions[i]
    if shift(ri, rj, di, dj):
        ri, rj = ri+di, rj+dj
    
for i in range(len(board)):
    print(''.join(board[i]))

gps = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == '[':
            gps += 100 * i + j
print(gps)
