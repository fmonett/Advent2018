
#https://en.wikipedia.org/wiki/Summed-area_table

grid = [[0 for i in range(0,300)] for j in range(0,300)]
satgrid = [[0 for i in range(0,300)] for j in range(0,300)]
serial=5093

for y in range(1,300):
    for x in range(1,300):
        rackid = x + 10
        power = rackid * y
        power += serial
        power *= rackid
        powerstr = str(power)
        if power < 100:
            power = -5
        else:
            power = int(powerstr[-3]) - 5
        
        satgrid[y][x] = power + (0 if y == 1 else satgrid[y-1][x]) + (0 if x == 1 else satgrid[y][x-1]) - (0 if x == 1 and y== 1 else satgrid[y-1][x-1])
        grid[y][x] = power
        
maxpower = -1
maxpos = ""

for x in range(0,300):
    for y in range(0,300):
        maxsquaresize = min(min(300-x,300),min(300-y,300))
        for s in range(1,maxsquaresize):
            power = satgrid[y+s][x+s] + satgrid[y][x] - satgrid[y][x+s] - satgrid[y+s][x]
                
            if power > maxpower:
                maxpower = power
                maxpos = "%i,%i,%i"%(x+1,y+1,s)
            
                        
print maxpos
