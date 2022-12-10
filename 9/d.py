import math

with open("input.txt") as f: i=f.readlines()

def distance(a,b): return math.sqrt(pow(a[0]-b[0],2)+pow(a[1]-b[1],2))
        
def p1(z):
    Y="DU"
    X="RL"
    STARTING_POS=[2,2]
    
    H=STARTING_POS.copy() # leading
    T=STARTING_POS.copy() # following 1 step behind
    
    been=[]
    for i in z:
        command=i.strip().split()
        for _ in range(int(command[1])):
            h=H.copy(); t=T.copy()
            h[0 if command[0] in X else 1]+=(1 if command[0]==(X[0] if command[0] in X else Y[0]) else -1)

            if distance(h,t)>=2: t=H.copy()
            if t not in been: been.append(t)
            H=h; T=t
            
    return len(been)

def c(a): return [x.copy() for x in a]

def m(a,b):
    ax,ay=a
    bx,by=b

    d=[min(1, max(-1, x)) for x in [ax-bx,ay-by]]
    if [ax-bx,ay-by]==d: return b
    else: return [bx+d[0], by+d[1]]
        


def p2(z):
    Y="DU"
    X="RL"
    STARTING_POS=[12,16]
    
    H=[STARTING_POS.copy() for _ in range(10)]
    
    been=[]
    for i in z:
        command=i.strip().split()
        for _ in range(int(command[1])):
            h=c(H)
            
            h[0][0 if command[0] in X else 1]+=(1 if command[0]==(X[0] if command[0] in X else Y[0]) else -1)
            
            for k in range(1,len(h)):
                h[k]=m(h[k-1],h[k])
                    
                    
            if h[-1] not in been: been.append(h[-1])
            H=c(h)  
    return len(been)