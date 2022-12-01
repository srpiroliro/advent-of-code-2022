from time import perf_counter 

start=perf_counter()

with open("input.txt") as f: raw=f.read()

calories=[
    sum([int(x) for x in g.split("\n")]) 
    for g in raw.split("\n\n")
]
calories.sort(reverse=True)
biggest=sum(calories[:3])

stop=perf_counter()
print(biggest, f"{stop-start}s elapsed")

#### 0.00048146297922357917s elapsed ####