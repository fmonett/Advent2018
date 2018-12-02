
twoof = 0
threeof = 0

with open('data2-1.txt', 'r') as data_file:
    lines = [line.strip() for line in data_file.readlines()]

for l in lines:
    for l2 in lines:
        numdiffs = 0
        diffpos = -1
        for i in range(0,len(l)):
            if l[i] != l2[i]:
                numdiffs += 1
                diffpos = i
                
        if numdiffs == 1:
            print l[:diffpos] + l[diffpos+1:]