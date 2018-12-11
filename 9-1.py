
list = [0]
curmarble = 1
curmarblepos = 0
nplayers = 410
players = {}
curplayer = 1

while curmarble <= 72059:
    if curmarble % 23 == 0:
        diff = 7 % len(list)
        if diff > curmarblepos:
            spos = len(list) - (diff - curmarblepos)
        else:
            spos = curmarblepos - diff
        curmarblepos = spos
        if curplayer not in players:
            players[curplayer] = 0
        
        players[curplayer] += curmarble + list[spos]
        
        list = list[:spos] + list[spos+1:]
    else:
        pos = (curmarblepos + 1) % len(list)
        curmarblepos = pos + 1
        list = list[:pos+1] + [curmarble] + list[pos+1:]
        
    curplayer += 1
    if curplayer > nplayers:
        curplayer = 1
        
    curmarble += 1
    
maxscore = -1
for p in players:
    if players[p] > maxscore:
        maxscore = players[p]
        
print maxscore