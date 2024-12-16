import sys
sys.setrecursionlimit(100000)
board = [list(r.strip()) for r in open('insmall2.txt').readlines()]

def find_piece(board, piece):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == piece:
                return i,j
    return None

si, sj = find_piece(board, 'S')
ei, ej = find_piece(board, 'E')

memo = {}
directions = [(0,1), (1,0),(0,-1),(-1,0)]
def find_path(board, si, sj, diridx, cost):
    if board[si][sj] == '#':
        return
    if (si, sj, diridx) in memo:
        if memo[(si, sj, diridx)] <= cost:
            return 
    memo[(si, sj, diridx)] = cost
    if board[si][sj] == 'E':
        return

    if board[si][sj] == '.' or board[si][sj] == 'S':
        ni, nj = si+directions[diridx][0], sj+directions[diridx][1]
        find_path(board, ni,nj,diridx, cost+1)
        # quick prune
        ni2, nj2 = si+directions[(diridx+1) % 4][0], sj+directions[(diridx + 1) % 4][1]
        if board[ni2][nj2] != '#':
            find_path(board, si,sj,(diridx+1)%4, cost+1000)
        ni2, nj2 = si+directions[(diridx-1) % 4][0], sj+directions[(diridx-1) % 4][1]
        if board[ni2][nj2] != '#':
            find_path(board, si,sj,(diridx-1)%4, cost+1000)
        #ni2, nj2 = si+directions[(diridx+2) % 4][0], sj+directions[(diridx+2) % 4][1]
        #if board[ni2][nj2] != '#':
        #    find_path(board, si,sj,(diridx+2)%4, cost+2000)
        # lets assume u-turning is generally going to be worse
    return

find_path(board, si, sj, 0, 0)
md = min([memo[(ei, ej, i)] for i in range(4) if (ei,ej,i) in memo])
print(md)
# we will need this for backtrack
import pickle
pickle.dump(memo, open('memosmall2.pickle', 'wb'))
