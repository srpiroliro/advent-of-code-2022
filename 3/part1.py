from time import perf_counter 
start=perf_counter()

#######  START  ########

cnt=0
with open("input.txt") as f: rucksacks=f.read().split()
for rucksack in rucksacks:
    c1, c2=rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]

    for i in list(set(c1)&set(c2)):
        o=ord(i)
        if o>=97: cnt+=o-96
        else: cnt+=o-65+27
print(cnt)

#######  END  ########

print(f"\n\n{perf_counter()-start}s elapsed")
#### s elapsed ####