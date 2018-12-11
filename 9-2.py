
class marble:
    def __init__(self,num):
        self.num = num
        self.prev = self
        self.next = self
        
first = marble(0)
curmarble = first

maxmarble = 72059 * 100
marblenum = 1
nplayers = 410
players = {}

while marblenum <= maxmarble:
    curplayer = marblenum % nplayers
    if curplayer not in players:
        players[curplayer] = 0
        
    ptr = curmarble
    if marblenum % 23 == 0:
        for i in range(0,7):
            ptr = ptr.prev
            
        players[curplayer] += marblenum + ptr.num
        ptr.prev.next = ptr.next
        ptr.next.prev = ptr.prev
        curmarble = ptr.next
    else:
        newmarble = marble(marblenum)
        old = curmarble.next.next
        newmarble.next = old
        old.prev = newmarble
        newmarble.prev = curmarble.next
        curmarble.next.next = newmarble
        curmarble = newmarble
    
           
    marblenum += 1    
    

maxscore = -1
for p in players:
    if players[p] > maxscore:
        maxscore = players[p]
        
print maxscore
    
