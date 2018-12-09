import re

insns = {}
pred = {}

class worker:
    def __init__(self):
        self.busy = False
        self.tasktime = 0
        self.curtask = ""
        
    def addtask(self,task):
        self.curtask = task;
        self.tasktime = 60 + (ord(task) - ord('A') + 1)
        self.busy = True
        
    def is_busy(self):
        return self.busy
        
    def tick(self):
        if self.busy:
            self.tasktime -= 1
            if self.tasktime == 0:
                self.busy = False
                return self.curtask
            else:
                return False
            
def dispatch(workers,task):
    for w in workers:
        if not w.is_busy():
            w.addtask(task)
            return True
            
    return False
            
def tickall(workers):
    res = []
    for w in workers:
        r = w.tick()
        if r:
            res.append(r)
            
    return res
    
def all_finished(workers):
    for w in workers:
        if w.is_busy():
            return False
            
    return True
    
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
workers = [worker() for i in range(0,5)]
curtick = 0

while not all_finished(workers) or len(avail) > 0:
    scheduled = []
    for a in avail:
        if is_allowed(a,pred,seq):
            if dispatch(workers,a):
                scheduled.append(a)
    
    newavail = []
    for a in avail:
        if a not in scheduled:
            newavail.append(a)
            
    avail = newavail
        
    avail.sort()
    
    res = tickall(workers)
    for r in res:
        seq += r
        if r in insns:
            for i in insns[r]:
                if i not in avail:
                    avail.append(i)
        avail.sort()
    
    curtick += 1

print seq
print curtick
      