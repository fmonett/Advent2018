import re

shifts = {}
curguard = ""

with open('data4-1-sorted.txt', 'r') as data_file:
    for line in data_file:
        line = line.strip()
        res = re.match("\[(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+)\]",line)
        vals = res.groupdict()
        
        for v in vals:
            vals[v] = int(vals[v])
                    
        status = line[len(res.group(0)):].strip()
        
        res = re.match("Guard #(\d+)",status)
        if res:
            #print "Begins %s" % res.group(1)

            if curguard != "":
                for min in range(lastmin + 1,60):
                    shifts[curguard][-1][min] = laststate

            curguard = res.group(1)
            if curguard not in shifts:
                shifts[curguard] = []
            
            shifts[curguard].append({})
            
            if vals['hour'] != 0:
                lastmin = 0
            else:
                lastmin = vals['minute']
                
            laststate = True
            shifts[curguard][-1][lastmin] = laststate
            
        if "wakes" in status:
            for min in range(lastmin + 1,vals['minute']):
                shifts[curguard][-1][min] = laststate
            
            shifts[curguard][-1][vals['minute']] = True
            laststate = True
            lastmin = vals['minute']
            #print "WAKES"
            
        if "asleep" in status:
            for min in range(lastmin + 1,vals['minute']):
                shifts[curguard][-1][min] = laststate
            
            shifts[curguard][-1][vals['minute']] = False
            laststate = False
            lastmin = vals['minute']
            #print "sleep"
            
        
maxtime = -1
maxguard = -1
for g in shifts:    
    ttltime = 0    
    for s in shifts[g]:
        for min in s:
            if s[min] == False:
                ttltime += 1
                
    if ttltime > maxtime:
        maxtime = ttltime
        maxguard = g
        
print "The best sleeper is #%s with %i hours" % (maxguard,maxtime)

topmins = {}
for s in shifts[maxguard]:
    for min in s:
        if min not in topmins:
            topmins[min] = 0
            
        if s[min] == False:
            topmins[min] += 1
            

maxreps = -1
maxmin = -1
for m in topmins:
    if topmins[m] > maxreps:
        maxreps = topmins[m]
        maxmin = m
        
print "The best time for sleepin' is minute %i" % maxmin
print "The answer is then %i" % (int(maxguard) * maxmin)