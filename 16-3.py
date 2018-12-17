
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
       
ops = {
0 : eqir,
1 : borr,
2 : addr,
3 : gtri,
4 : muli,
5 : gtir,
6 : mulr,
7 : banr,
8 : bori,
9 : eqri,
10 : eqrr,
11 : bani,
12 : setr,
13 : gtrr,
14 : addi,
15 : seti}

state = [0,0,0,0]
with open('data16-2.txt', 'r') as data_file:
    while True:
        line = data_file.readline()
        if line == "":
            break
            
        line = line.strip()
        dat = line.split(" ")
        insn = {'opcode': int(dat[0]),'a' : int(dat[1]),'b' : int(dat[2]),'c': int(dat[3])}
        ops[insn['opcode']](state,insn)
        
    print state