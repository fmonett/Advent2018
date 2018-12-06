
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

size = 0
for y in range(miny-1,maxy + 2):
    for x in range(minx-1,maxx + 2):
        sum = 0
        for n,c in enumerate(coords):
            dist = abs(x - c[0]) + abs(y - c[1])
            sum += dist
                   
        if sum < 10000:
            size += 1
        
print size
        