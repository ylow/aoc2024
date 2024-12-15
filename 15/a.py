board = [list(r.strip()) for r in open('in_board.txt').readlines()]
moves = open('in_moves.txt').read()

def shift(i,j,di,dj):
    ti,tj = i+di,j+dj
    if board[ti][tj] == '#':
        return False
    elif board[ti][tj] == '.':
        board[ti][tj] = board[i][j]
        board[i][j] = '.'
        return True
    elif board[ti][tj] == 'O':
        if shift(ti,tj,di,dj):
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
        if board[i][j] == 'O':
            gps += 100 * i + j
print(gps)
