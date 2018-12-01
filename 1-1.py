
total = 0
with open('data1-1.txt', 'r') as data_file:
    for line in data_file:
        line = line.strip()
        
        if line[0] == "-":
            total -= int(line[1:])
        else:
            total += int(line[1:])
            
print total