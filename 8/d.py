import os

with open("input.txt") as f: inpt=f.readlines()


def p1(z):
    table=[list(i.strip()) for i in z]
    visibles=0
    for i,y in enumerate(table[1:-1],start=1):
        for g,x in enumerate(y[1:-1],start=1):
            target=x
            for u in [[o[g] for o in table[0:i]], [o[g] for o in table[i+1:len(table)]], table[i][0:g], table[i][g+1:len(table[i])]]:
                if max(u)<target:
                    visibles+=1
                    break
    visibles+=len(table)*2+(len(table)-2)*2
    return visibles
        
def p2(z):
    table=[list(i.strip()) for i in z]
    visibles=[]
    for i,y in enumerate(table[1:-1],start=1):
        for g,x in enumerate(y[1:-1],start=1):
            target=x
            look_up=[o[g] for o in table[0:i]]; look_up.reverse()
            look_down=[o[g] for o in table[i+1:len(table)]]
            look_left=table[i][0:g]; look_left.reverse()
            look_right=table[i][g+1:len(table[i])]
            v=1
            for u in [look_up, look_down, look_left, look_right]:
                for l,o in enumerate(u,start=1):
                    if o>=target: break
                v*=l
            visibles.append(v)
    return max(visibles)

print(p2(inpt))