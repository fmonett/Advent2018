
map = []

def surround(map,pos):
    counts = {'#' : 0,'|' : 0,'.' : 0}
    for y in range(max(0,pos[1]-1),min(len(map)-1,pos[1]+1)+1):
        line = ""
        for x in range(max(0,pos[0]-1),min(len(map[0])-1,pos[0]+1)+1):
            if pos[0] == x and pos[1] == y:
                continue
                
            counts[map[y][x]] += 1
        
    return counts
    
def draw(map):
    for m in map:
        print m
        
    print "\n\n"

def count(map):
    lumber = 0
    wood = 0
    for m in map:
        for l in m:
            if l == "#":
                lumber += 1
                
            if l == "|":
                wood += 1
                
    return lumber * wood
    
def next(map):
    newmap = []
    for y in range(0,len(map)):
        line = ""
        for x in range(0,len(map[0])):
            c = surround(map,[x,y])
            v = map[y][x]
            nv = v
            
            if v == ".":
                if c["|"] >= 3:
                    nv = "|"
                else:
                    nv = "."
            elif v == "|":
                if c["#"] >= 3:
                    nv = "#"
                else:
                    nv = "|"
            elif v == "#":
                if c["#"] >= 1 and c["|"] >= 1:
                    nv = "#"
                else:
                    nv = "."
                    
            line += nv
        newmap.append(line)

    return newmap
        
with open('data18-1.txt', 'r') as data_file:
    for line in data_file:
        map.append(line.strip())

for i in range(0,10):
    map = next(map)
    
print count(map)