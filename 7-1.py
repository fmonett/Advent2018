import re

insns = {}
pred = {}

def is_allowed(step,pred,seq):
    if step in pred:
        for p in pred[step]:
            if p not in seq:
                return False
                
    return True
    
with open('data7-1.txt', 'r') as data_file:
 for line in data_file:
  line = line.strip()
  match = re.match("Step ([A-Z]) must be finished before step ([A-Z]) can begin",line)
  if match.group(1) not in insns:
      insns[match.group(1)] = [match.group(2)]
  else:
      insns[match.group(1)].append(match.group(2))
      
  if match.group(2) not in pred:
      pred[match.group(2)] = [match.group(1)]
  else:
      pred[match.group(2)].append(match.group(1))

avail = []
for i in range (0,26):
    ltr = chr(ord('A') + i)
    if ltr in insns and ltr not in pred:
        avail.append(ltr)
        
avail.sort()
seq = ""

while len(avail) > 0:
    step = avail[0]
    avail = avail[1:]
    if is_allowed(step,pred,seq):
        seq += step
        
        if step in insns:
            for i in insns[step]:
                if i not in avail:
                    avail.append(i)

                
        avail.sort()

print seq
      