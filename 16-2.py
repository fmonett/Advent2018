
def addr(state,insn):
    state[insn['c']] = state[insn['a']] + state[insn['b']]
    
def addi(state,insn):
    state[insn['c']] = state[insn['a']] + insn['b']

def mulr(state,insn):
    state[insn['c']] = state[insn['a']] * state[insn['b']]
    
def muli(state,insn):
    state[insn['c']] = state[insn['a']] * insn['b']
    
def banr(state,insn):
    state[insn['c']] = state[insn['a']] & state[insn['b']]
    
def bani(state,insn):
    state[insn['c']] = state[insn['a']] & insn['b']

def borr(state,insn):
    state[insn['c']] = state[insn['a']] | state[insn['b']]
    
def bori(state,insn):
    state[insn['c']] = state[insn['a']] | insn['b']
    
def setr(state,insn):
    state[insn['c']] = state[insn['a']]
    
def seti(state,insn):
    state[insn['c']] = insn['a']
    
def gtir(state,insn):
    state[insn['c']] = 1 if insn['a'] > state[insn['b']] else 0

def gtri(state,insn):
    state[insn['c']] = 1 if state[insn['a']] > insn['b'] else 0
    
def gtrr(state,insn):
    state[insn['c']] = 1 if state[insn['a']] > state[insn['b']] else 0

def eqir(state,insn):
    state[insn['c']] = 1 if insn['a'] == state[insn['b']] else 0

def eqri(state,insn):
    state[insn['c']] = 1 if state[insn['a']] == insn['b'] else 0
    
def eqrr(state,insn):
    state[insn['c']] = 1 if state[insn['a']] == state[insn['b']] else 0
    
opcodes = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]
txtopcodes = ["addr","addi","mulr","muli","banr","bani","borr","bori","setr","seti","gtir","gtri","gtrr","eqir","eqri","eqrr"]
counts = {}

def test(insn,before,after):
    for c,o in enumerate(opcodes):
        if insn['opcode'] not in counts:
            counts[insn['opcode']] = {}
            
        state = list(before)
        o(state,insn)
        if state == after:
            if txtopcodes[c] not in counts[insn['opcode']]:
                counts[insn['opcode']][txtopcodes[c]] = 1
            else:
                counts[insn['opcode']][txtopcodes[c]] += 1
    
total = 0
with open('data16-1.txt', 'r') as data_file:
    while True:
        line = data_file.readline()
        before = eval(line.strip().split(":")[1])
        line = data_file.readline().strip()
        dat = line.split(" ")
        insn = {'opcode': int(dat[0]),'a' : int(dat[1]),'b' : int(dat[2]),'c': int(dat[3])}
        line = data_file.readline()
        after = eval(line.strip().split(":")[1])
        
        test(insn,before,after)
        
        line = data_file.readline()
        if line == "":
            break
       
#print counts
sets = {}       
for c in counts:
    maxval = max([counts[c][x] for x in counts[c]])
    res = set()
    for x in counts[c]:
        if counts[c][x] == maxval:
            res.add(x)
    sets[c] = res

removed = True    
while removed:
    removed = False
    for c,s in enumerate(sets):
        if len(sets[s]) == 1:
            for c2,s2 in enumerate(sets):
                if c2 != c:
                    if list(sets[s])[0] in sets[s2]:
                        removed = True
                        sets[s2].remove(list(sets[s])[0])
code = "ops = {\n"                    
for s in sets:
    if len(sets[s]) > 1:
        print "%s has more that 1 possibility!!"
        
    code += "%s : %s,\n" % (s,list(sets[s])[0])
code += "}\n"
print code