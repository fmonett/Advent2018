
strdata = open("data8-1.txt").read().strip().split(" ")
data = [int(x) for x in strdata]

def decode(data,pos):
    opos = pos
    nchild = data[pos]
    pos += 1
    nmeta = data[pos]
    pos += 1
    sum = 0
    
    for c in range(0,nchild):
        length,childsum = decode(data,pos)
        pos += length
        sum += childsum
        
        
    for m in range(0,nmeta):
        sum += data[pos]
        pos += 1
        
    return (pos-opos,sum)
    
    
length,sum = decode(data,0)

print sum

