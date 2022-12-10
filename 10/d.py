with open("input.txt") as f: i=f.readlines()
def p1(x):
    cs=[]
    X=cycle=1
    jump=cnt=0
    
    while cnt<len(x):
        command=x[cnt].strip()
        cycle+=1

        if jump:
            X+=int(command.split()[-1])
            jump=False  
        else: jump="addx" in command
        if(cycle+20)%40==0: cs.append(cycle*X)
        if not jump: cnt+=1

    return sum(cs)

def p2(x):
    X=cycle=1
    jump=False
    
    cnt=0
    row=""
    while cnt<len(x):
        command=x[cnt].strip()        
        sprite=list(range(X-1,X+2))

        row+="#" if (cycle-1)%40 in sprite else "."
        if jump:
            X+=int(command.split()[-1])
            jump=False
        else: jump="addx" in command
        
        if(cycle)%40==0: row+="\n"
        if not jump: cnt+=1
            
        cycle+=1
    return row