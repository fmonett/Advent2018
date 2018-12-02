
twoof = 0
threeof = 0

with open('data2-1.txt', 'r') as data_file:
    for line in data_file:
        line = line.strip()
         
        freq = {}
        for c in line:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
                
        for f in freq:
            if freq[f] == 2:
                twoof += 1
                break
                
        for f in freq:
            if freq[f] == 3:
                threeof += 1
                break
print twoof
print threeof
print twoof * threeof