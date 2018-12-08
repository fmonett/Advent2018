
strdata = open("data8-1.txt").read().strip().split(" ")
data = [int(x) for x in strdata]

def decode(data,pos):
    opos = pos
    nchild = data[pos]
    pos += 1
    nmeta = data[pos]
    pos += 1
    sum = 0
    
    csums = []
    for c in range(0,nchild):
        length,childsum = decode(data,pos)
        pos += length
        csums.append(childsum)
        
    for m in range(0,nmeta):
        if nchild > 0:
            cidx = data[pos] - 1
            if cidx < len(csums):
                sum += csums[cidx]
        else:
            sum += data[pos]

        pos += 1
        
    return (pos-opos,sum)
    
    
len,sum = decode(data,0)

print sum

