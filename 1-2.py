import sys

total = 0
totals = {0:1}

with open('data1-1.txt', 'r') as data_file:
    while True:
        data_file.seek(0)
        for line in data_file:
            line = line.strip()
           # print line
            if line[0] == "-":
                total -= int(line[1:])
            else:
                total += int(line[1:])
            
            if total in totals:
                print total
                sys.exit(0)
            else:
                totals[total] = 1
            