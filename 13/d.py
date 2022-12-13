import json
from functools import cmp_to_key

with open("input.txt") as f: i=f.read()

def p1(x):
    correct=0
    for pair,group in enumerate(x.strip().split("\n\n"),start=1):
        left,right=[json.loads(x) for x in group.splitlines()]
        if compare(left,right)>0:correct+=pair
    return correct

def p2(x):
    groups=[json.loads(i) for i in x.replace("\n\n","\n").splitlines()]
    dividers=[[[2]], [[6]]]
    groups+=dividers
    groups.sort(key=cmp_to_key(compare), reverse=True)
    return (groups.index(dividers[0])+1)*(groups.index(dividers[1])+1)
    
def compare(x,y):
    if type(x)==int and type(y)==int: return y-x
    elif type(x)==int: return compare([x],y)
    elif type(y)==int: return compare(x,[y])
    else: 
        for i in range(max(len(x), len(y))):
            if i<len(x) and i<len(y):
                c=compare(x[i],y[i])
                if not c==0: return c
            elif i>=len(x) and i<len(y): return 1
            else: return -1
        return 0