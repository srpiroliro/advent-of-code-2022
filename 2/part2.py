from time import perf_counter 
start=perf_counter()

#######  START  ########
with open("input.txt") as f: raw=f.read()
result=0
r={
    "Z":{"A":"Y", "B":"Z", "C":"X"},
    "X":{"A":"Z", "B":"X", "C":"Y"},
    "Y":{"A":"X", "B":"Y", "C":"Z"}
}
hands={"X":1, "Y":2, "Z":3}

play_log=raw.split("\n")
for p in play_log:
    hs=p.split(" ")
    
    result+=(hands[hs[1]]-1)*3+hands[r[hs[1]][hs[0]]]
    
#######  END  ########


print(result, f"{perf_counter()-start}s elapsed")
#### 0.01238319801632315s elapsed ####