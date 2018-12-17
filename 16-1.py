
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

def test(insn,before,after):
    fit = 0
    for o in opcodes:
        state = list(before)
        o(state,insn)
        if state == after:
            fit += 1
    return fit
    
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
        
        if test(insn,before,after) >= 3:
            total += 1
        
        line = data_file.readline()
        if line == "":
            break
       
        
print total