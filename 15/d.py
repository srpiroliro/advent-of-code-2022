from pprint import pprint
with open("test.txt") as f: i=f.read()

def manhattan(a,b):
    return sum([abs(x1-x2) for x1,x2 in zip(a,b)])

def get_pair(line):
    line=line.strip().replace("Sensor at ","").replace(" closest beacon is at ","").replace("x=","").replace("y=","")
    return [[int(i) for i in o.split(", ")] for o in line.split(":")]

def get_lows_n_highs(inpt):
    m=inpt.replace(": closest beacon is at ", "\n").replace("Sensor at ","").splitlines()
    coords=[]
    for c in m:
        a,b=c.split(",")
        coords.append([int(a.split("=")[1]), int(b.split("=")[1])])
        
    xs=[o[0] for o in coords]; ys=[o[1] for o in coords]
        
    return [min(xs),min(ys)], [max(xs),max(ys)]


class coords:
    def __init__(self,x,y) -> None:
        self.x=x; self.y=y

def p1(inpt):
    Y2check=10
    x_touching=set()
    
    ls,hs=get_lows_n_highs(inpt)
    
    xs=[ls[0],hs[0]] #
    for line in inpt.splitlines():
        sensor,beacon=get_pair(line)
        
        if sensor==[8,7] or True:
            md=manhattan(sensor,beacon)
            y_range=range(sensor[1]-md, sensor[1]+md)
            if Y2check in list(y_range):
                dif=md+(sensor[1]-Y2check)
                
                for i in range(sensor[0]-dif, sensor[0]+dif+1):
                    x_touching.add(coords(i,Y2check))
                
                x=[sensor[0]-md, sensor[0]+md]
                if xs[0]>x[0]: xs[0]=x[0]
                if xs[1]<x[1]: xs[1]=x[1]
    
    print("min:",xs[0], "max:",xs[1])
    big_dif=xs[1]-xs[0]
    print(big_dif,len(x_touching), big_dif-len(x_touching))
    
    
    
    
    
    
print(p1(i))