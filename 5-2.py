
strd = open("data5-1.txt").read().strip()

def do_reaction(strd):
    stack = []
    for chr in strd:
        if len(stack) == 0:
            stack.append(chr)
        else:
            if chr.upper() == stack[-1].upper() and  (chr.isupper() and stack[-1].islower() or chr.islower() and stack[-1].isupper()):
                stack.pop()
            else:
                stack.append(chr)
            
    return "".join(stack)

minlen = len(strd)    
for i in range (ord('a'),ord('z') + 1):
    tempstr = strd.replace(chr(i),"")
    tempstr = tempstr.replace(chr(i).upper(),"")
    
   
    res = do_reaction(tempstr)
    minlen = min(minlen,len(res))
        
        
print minlen
        
    
    