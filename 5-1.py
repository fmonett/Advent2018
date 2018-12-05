
strd = open("data5-1.txt").read().strip()
stack = []

for chr in strd:
    if len(stack) == 0:
        stack.append(chr)
    else:
        if chr.upper() == stack[-1].upper() and  (chr.isupper() and stack[-1].islower() or chr.islower() and stack[-1].isupper()):
            stack.pop()
        else:
            stack.append(chr)
            
print len(stack)