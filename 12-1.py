
with open('data12-1.txt', 'r') as data_file:
    lines = data_file.readlines()
    lines = [l.strip() for l in lines]
    
initial = lines[0].split(":")[1].strip()

rules = {}
board = {}

for i in range(0,len(initial)):
    board[i] = initial[i]

for i in range(2,len(lines)):
    elems = lines[i].split("=>")
    rules[elems[0].strip()] = elems[1].strip()

    boardlen = len(initial)

for x in range(0,20):
    newboard = {}
    line = ""
    for i in range(-3,boardlen + 20):
        if i in board:
            line += board[i]
        else:
            line += "."

    last = boardlen
    for i in range(-5,boardlen + 6):
        substr = ""
        for off in range(-2,3):
            if i+off in board:
                substr += board[i+off]
            else:
                substr += "."

        if substr in rules:
            if rules[substr] == "#":
                last = i
            newboard[i] = rules[substr]
        else:
            newboard[i] = "."
            
    board = newboard
    boardlen = last
    print last
    
score = 0
for p in board:
    if board[p] == '#':
        score += p
    
print score
        