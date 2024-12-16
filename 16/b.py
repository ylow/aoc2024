import pickle
memo = pickle.load(open('memo.pickle', 'rb'))

import sys
sys.setrecursionlimit(100000)
board = [list(r.strip()) for r in open('in.txt').readlines()]

def find_piece(board, piece):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == piece:
                return i,j
    return None

si, sj = find_piece(board, 'S')
ei, ej = find_piece(board, 'E')
directions = [(0,1), (1,0),(0,-1),(-1,0)]

bestset = set()
def backtrack(board, si, sj, diridx, curcost):
    if board[si][sj] == '#':
        return
    bestset.add((si,sj))
    if board[si][sj] == 'S':
        return
    if board[si][sj] == '.' or board[si][sj] == 'E':
        ni, nj = si-directions[diridx][0], sj-directions[diridx][1]
        if memo.get((ni,nj,diridx), -100000) == curcost - 1:
            backtrack(board, ni, nj, diridx, curcost-1)
        if memo.get((si,sj,(diridx+1) % 4), -100000) == curcost - 1000:
            backtrack(board, si, sj, (diridx+1) % 4, curcost-1000)
        if memo.get((si,sj,(diridx-1) % 4), -100000) == curcost - 1000:
            backtrack(board, si, sj, (diridx-1) % 4, curcost-1000)
    return
md = min([memo[(ei, ej, i)] for i in range(4) if (ei,ej,i) in memo])
for diridx in range(4):
    if (ei,ej,diridx) in memo and memo[(ei,ej,diridx)] == md:
        print(ei,ej,diridx, memo[(ei,ej,diridx)])
        backtrack(board, ei, ej, diridx, memo[(ei,ej,diridx)])

print(len(bestset))
