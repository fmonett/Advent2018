
e1pos = 0
e2pos = 1
board = [3,7]
nrecipies = 147061

for i in range(0,nrecipies + 10):
    total = board[e1pos] + board[e2pos]
    strt = str(total)
    for c in strt:
        board.append(int(c))
    e1pos = (e1pos + board[e1pos] + 1) % len(board)
    e2pos = (e2pos + board[e2pos] + 1) % len(board)
   
res = ""
for i in range(nrecipies,nrecipies+10):
    res += str(board[i])
    
print res
   