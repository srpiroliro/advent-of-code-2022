with open("input.txt") as f: ranges=f.read().split()

def part1():
    def c(n1,n2): return int(n1[0])>=int(n2[0]) and int(n1[1])<=int(n2[1])
    cnt=0
    for r in ranges:
        rgs=r.replace(",","-").split("-")
        if c(rgs[0:2],rgs[2:]) or c(rgs[2:],rgs[0:2]): cnt+=1
    return cnt


def part2():
    cnt=0
    for r in ranges:
        rgs=[int(i) for i in r.replace(",","-").split("-")]
        r1=range(rgs[0],rgs[1]+1)
        r2=range(rgs[2],rgs[3]+1)
        
        if len(set(r1)&set(r2))>0: cnt+=1
    return cnt