grid = {}
serial=5093

for x in range(1,301):
    for y in range(1,301):
        rackid = x + 10
        power = rackid * y
        power += serial
        power *= rackid
        powerstr = str(power)
        if power < 100:
            power = -5
        else:
            power = int(powerstr[-3]) - 5
            
        grid["%i,%i"%(x,y)] = power

maxpower = -1
maxpos = ""
        
for x in range(1,298):
    for y in range(1,298):
        total = 0
        for xo in range(0,3):
            for yo in range(0,3):
                total += grid["%i,%i"%(x + xo,y + yo)]
                
        if total > maxpower:
            maxpower = total
            maxpos = "%i,%i"%(x,y)
            
print maxpos