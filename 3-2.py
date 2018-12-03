import re

board = {}
stomped = {}

with open('data3-1.txt', 'r') as data_file:
    for line in data_file:
        matches = re.match("#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)",line)
        id = int(matches.group(1))
        left = int(matches.group(2))
        top = int(matches.group(3))
        width = int(matches.group(4))
        height = int(matches.group(5))
        
        stomped[id] = False
        
        for x in range(left,left + width):
            for y in range(top,top + height):
                coords = "%i-%i" % (x,y)
                if coords not in board:
                    board[coords] = [1,id]
                else:
                    board[coords][0] += 1
                    stomped[board[coords][1]] = True
                    stomped[id] = True
        
        
for s in stomped:
    if stomped[s] == False:
        print s
