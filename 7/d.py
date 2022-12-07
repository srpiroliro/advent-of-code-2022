import os

with open("input.txt") as f: inpt=f.readlines()
    
def pj(a,b):
    if not a or b=="/": return b
    elif b=="..": 
        t=a.rsplit("/",1)[0]
        return t if t else "/"
    else: return os.path.join(a,b)

def p1(x):
    def calc_size(y):
        sze=0
        for c in directories[y]: sze+=int(c[0]) if not "dir"==c[0] else calc_size(c[1])
        new_directories[y]={"size":sze, "contents":directories[y]}
        return sze
    
    directories=new_directories={}
    
    current_path=""
    for i,line in enumerate(x):
        if line.startswith("$"):
            command=line.replace("$","").strip()
            
            if "cd" in command:
                current_path=pj(current_path,command.split()[-1])
            elif "ls" in command:
                contents=[]
                print("contents of",current_path)
                c=i+1
                while "$" not in x[c]:
                    tpe,name=x[c].strip().split()
                    if tpe=="dir": name=os.path.join(current_path,name)
                    contents.append([tpe,name])
                    c+=1
                    if c==len(x): break
                directories[current_path]=contents
       
    calc_size("/")
    
    total_size=0
    for i in new_directories:
        if new_directories[i]["size"]<100000: total_size+=new_directories[i]["size"]
    
    return total_size

def p2(x):
    filesystem=70000000
    needed_unused=30000000
    directories=new_directories={}
    current_path=""
    
    def calc_size(y):
        sze=0
        for c in directories[y]: sze+=int(c[0]) if not "dir"==c[0] else calc_size(c[1])
        new_directories[y]={"size":sze, "contents":directories[y]}
        return sze
    
    for i,line in enumerate(x):
        if line.startswith("$"):
            command=line.replace("$","").strip()
            
            if "cd" in command:
                current_path=pj(current_path,command.split()[-1])
            elif "ls" in command:
                contents=[]
                c=i+1
                while "$" not in x[c]:
                    tpe,name=x[c].strip().split()
                    if tpe=="dir": name=os.path.join(current_path,name)
                    contents.append([tpe,name])
                    c+=1
                    if c==len(x): break
                directories[current_path]=contents
       
    calc_size("/")
    directories=new_directories
    to_delete=needed_unused-(filesystem-directories["/"]["size"])

    vals=[directories[i]["size"] for i in directories]
    vals.sort()

    for i in vals:
        if i>to_delete:
            return i