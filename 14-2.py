import sys

e1pos = 0
e2pos = 1
board = [3,7]
target = "147061"
i = 0

while True:
    total = board[e1pos] + board[e2pos]
    strt = str(total)
    for c in strt:
        board.append(int(c))
        if "".join([str(x) for x in board[-len(target):]]) == target:
            print len(board) - len(target)
            sys.exit(0)
        
    e1pos = (e1pos + board[e1pos] + 1) % len(board)
    e2pos = (e2pos + board[e2pos] + 1) % len(board)
    
    i += 1
   