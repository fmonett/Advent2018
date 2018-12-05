import re

destlines = []
with open('data4-1.txt', 'r') as data_file:
    for line in data_file:
        line = line.strip()
        res = re.match("\[(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+)\]",line)
        vals = res.groupdict()
        
        for v in vals:
            vals[v] = int(vals[v])
            
        hashcode = vals['month'] * 1000000 + vals['day'] * 10000 + vals['hour'] * 100 + vals['minute']
        destlines.append([hashcode,line])
        
        
destlines.sort(key=lambda x:x[0])
for l in destlines:
    print l[1]