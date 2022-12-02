from time import perf_counter 
start=perf_counter()

#######  START  ########

result=0
scores={"X":1, "Y":2, "Z":3}
outcome={"win":6, "draw":3, "lost":0}
win={"A":"Y", "B":"Z", "C":"X", "X":"B", "Y":"C", "Z":"A"}
with open("input.txt") as f: raw=f.read()

play_log=raw.split("\n")
for p in play_log:
    hs=p.split(" ")
    result+=scores[hs[1]]+outcome["win" if win[hs[0]]==hs[1] else ("lost" if win[hs[1]]==hs[0] else "draw")]

#######  END  ########


print(result, f"{perf_counter()-start}s elapsed")
#### 0.013347847969271243s elapsed ####