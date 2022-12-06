with open("input.txt") as f: inpt=f.read()

def p1(x):
    for i,ch in enumerate(x):
        if len(set(x[i:min(i+4, len(x))]))==4: return i+4
    
def p2(x):
    for i,ch in enumerate(x):
        if len(set(x[i:min(i+14, len(x))]))==14: return i+14
