from pprint import pprint

with open("input.txt") as f: inpt=f.read()

def get_stack(stacks):
    stacks.reverse()

    stack=[]
    for h,stk in enumerate(stacks):
        columns=[stk[i:i+4].strip().replace("[", "").replace("]", "") for i in range(0, len(stk), 4)]
        if h==0: stack=[[] for x in columns]
        else: [stack[i].append(c) if c else None for i,c in enumerate(columns)]
        
    return stack

def p1(inpt):
    stacks,instructions=inpt.split("\n\n", 1)
    stack=get_stack(stacks.split("\n"))

    for instruction in instructions.split("\n"):
        _, howmuch, _, fromc, _, toc=instruction.split()
        fromc=int(fromc)-1
        toc=int(toc)-1
        
        for i in range(int(howmuch)):
            stack[toc].append(stack[fromc][-1])
            del stack[fromc][-1]

    print("".join(["" if not i else i[-1] for i in stack]))
    
def p2(inpt):
    stacks,instructions=inpt.split("\n\n", 1)
    stack=get_stack(stacks.split("\n"))

    for instruction in instructions.split("\n"):
        _, howmuch, _, fromc, _, toc=instruction.split()
        fromc=int(fromc)-1
        toc=int(toc)-1
        howmuch=int(howmuch)
        
        for i in range(howmuch):
            x=i-howmuch
            stack[toc].append(stack[fromc][x])
            del stack[fromc][x]

    print("".join(["" if not i else i[-1] for i in stack]))