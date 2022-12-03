from time import perf_counter 
start=perf_counter()

#######  START  ########

cnt=line=0
with open("input.txt") as f: rucksacks=f.read().split()
while line<len(rucksacks):
    c1, c2, c3=rucksacks[line:line+3]

    for i in list(set(c1)&set(c2)&set(c3)):
        o=ord(i)
        if o>=97: cnt+=o-96
        else: cnt+=o-65+27
    
    line+=3
print(cnt)

#######  END  ########

print(f"{perf_counter()-start}s elapsed")
#### s elapsed ####