from math import prod
with open("input.txt") as f: i=f.read()

def p1(x):
    instructions=x.split("\n\n")
    monkeys=[]
    
    for i in instructions:
        parts=i.split("\n")
        
        monkeys.append({
            "items": [int(o) for o in parts[1].split(":")[-1].strip().split(", ")],
            "op":parts[2].split(": ")[-1].split("=")[-1].strip(),
            "divisible":int(parts[3].split("by")[-1].strip()),
            "t":int(parts[4].split("monkey")[-1].strip()),
            "f":int(parts[5].split("monkey")[-1].strip())
        })
    
    inspections=[0 for _ in range(len(monkeys))]
    
    for _ in range(20):
        for i,m in enumerate(monkeys):
            l=len(m["items"])
            inspections[i]+=l
            for _ in range(l):
                w=eval(m["op"].replace("old", str(monkeys[i]["items"].pop(0)//3)))
                monkeys[m["t"] if w%m["divisible"]==0 else m["f"]]["items"].append(w)

    inspections.sort(reverse=True)
    return inspections[0]*inspections[1]


def p2(x):
    instructions=x.split("\n\n")
    monkeys=[]
    
    for i in instructions:
        parts=i.split("\n")
        
        monkeys.append({
            "items": [int(o) for o in parts[1].split(":")[-1].strip().split(", ")],
            "op":parts[2].split(": ")[-1].split("=")[-1].strip(),
            "divisible":int(parts[3].split("by")[-1].strip()),
            "t":int(parts[4].split("monkey")[-1].strip()),
            "f":int(parts[5].split("monkey")[-1].strip())
        })
    
    inspections=[0 for _ in range(len(monkeys))]
    d=prod(m["divisible"] for m in monkeys)
    
    for _ in (range(10000)):
        for i,m in enumerate(monkeys):
            l=len(m["items"])
            inspections[i]+=l
            for _ in range(l):
                num=monkeys[i]["items"].pop(0)%d
                w=eval(m["op"], {}, {"old":num})

                monkeys[m["t"] if w%m["divisible"]==0 else m["f"]]["items"].append(w)

    inspections.sort(reverse=True)
    return inspections[0]*inspections[1]
