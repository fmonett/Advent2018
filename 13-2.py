import sys

map = []
cartdirs = ["^",">","v","<"]
dirs = [[0,-1],[1,0],[0,1],[-1,0]]
carts = []

class cart:
    def __init__(self,pos,dir):
        self.pos = pos
        self.dir = cartdirs.index(dir)
        self.turn = 0
        
    def left(self):
        self.dir -= 1
        if self.dir < 0:
            self.dir = len(dirs) -1
            
    def right(self):
        self.dir += 1
        if self.dir >= len(dirs):
            self.dir = 0
    
    def move(self):
        vdir = dirs[self.dir]
        self.pos[0] += vdir[0]
        self.pos[1] += vdir[1]
        
    def tick(self):
        c = map[self.pos[1]][self.pos[0]]
            
        if c == "/":
            if self.dir == 0 or self.dir == 2:
                self.right()
            elif self.dir == 3 or self.dir == 1:
                self.left()
        elif c == "\\":
            if self.dir == 3 or self.dir == 1:
                self.right()
            elif self.dir == 0 or self.dir == 2:
                self.left()
        elif c == "+":
            if self.turn == 0:
                self.left()
            elif self.turn == 2:
                self.right()
                
            self.turn = (self.turn + 1) % 3
            
        self.move()
                
                    
with open('data13-1.txt', 'r') as data_file:
    lines = data_file.readlines()
    lines = [l.rstrip('\r\n') for l in lines]
    
for line in lines:
    mapline = []
    for c in line:
        if c in cartdirs:
            print "Cart at (%i,%i)"%(len(mapline),len(map))
            carts.append(cart([len(mapline),len(map)],c))
            if c == "^" or c == "v":
                mapline.append("|")
            else:
                mapline.append("-")
        else:
            mapline.append(c)
            
    map.append(mapline)
    
        
while True:       
    if len(carts) == 1:
        print "Last cart remaining at %i,%i"%(carts[0].pos[0],carts[0].pos[1])
        sys.exit(0)
    
    carts.sort(key = lambda x: x.pos[0])
    carts.sort(key = lambda x: x.pos[1])
    
    for c in carts:
        c.tick()    
        
        toremove = []
        for c1,c in enumerate(carts):
            for c2,d in enumerate(carts):
                if c1 != c2 and c.pos == d.pos:
                    print "Collision at %i,%i"%(c.pos[0],c.pos[1])
                    toremove.append(c1)
                    toremove.append(c2)
        
        newcarts = []
        for c1,c in enumerate(carts):
            if c1 not in toremove:
                newcarts.append(c)
        carts = newcarts
   