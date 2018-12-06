
with open('data6-1.txt', 'r') as data_file:
    txcoords = [x.strip() for x in data_file.readlines()]
    
coords = []
for c in txcoords:
    ln = c.split(",")
    coords.append([int(ln[0]),int(ln[1])])
    
minx = reduce(min,map(lambda x:x[0],coords))
maxx = reduce(max,map(lambda x:x[0],coords))

miny = reduce(min,map(lambda x:x[1],coords))
maxy = reduce(max,map(lambda x:x[1],coords))

extremes = []

for n,c in enumerate(coords):
    if c[0] == minx or c[0] == maxx or c[1] == miny or c[1] == maxy:
        extremes.append(n)

counts = {}
for y in range(miny-1,maxy + 2):
    for x in range(minx-1,maxx + 2):
        lowest = 999999
        lows = []
        for n,c in enumerate(coords):
            dist = abs(x - c[0]) + abs(y - c[1])
           
            if dist < lowest:
                lowest = dist
        
            lows.append(dist)
        
        lcount = 0
        low = -1
        for n,l in enumerate(lows):            
            if l == lowest:
                lcount += 1
                low = n
                
        if lcount == 1:
            if low not in counts:
                counts[low] = 1
            else:
                counts[low] += 1
        
max = -1
for c in counts:
    if c in extremes:
        continue
    else:
        if counts[c] > max:
            max = counts[c]

print max            
            
        
        