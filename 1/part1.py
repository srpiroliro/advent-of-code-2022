from time import perf_counter 

start=perf_counter()

with open("input.txt") as f: raw=f.read()
biggest=0
for g in raw.split("\n\n"):
    calories=sum([int(x) for x in g.split("\n")])
    if biggest<calories: biggest=calories

stop=perf_counter()
print(biggest, f"{stop-start}s elapsed")

#### 0.0005120289861224592s elapsed ####