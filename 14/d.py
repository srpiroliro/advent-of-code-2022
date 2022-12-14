with open("input.txt") as f: i=f.read()

def get_lows_n_highs(inp):
    all_coords=inp.replace(" -> ", "\n").splitlines()+["500,0"] # sand cords
    xs=[int(x.split(",")[0]) for x in all_coords]; xs.sort()
    ys=[int(y.split(",")[1]) for y in all_coords]; ys.sort()
    
    return [xs[0],ys[0]], [xs[-1],ys[-1]]

def build_walls(inp, game, minimum):
    for line in inp.splitlines():
        commands=[[int(o) for o in l.split(",")] for l in line.split(" -> ")]
        for i in range(1,len(commands)):
            a,b=sorted([commands[i-1],commands[i]])

            for Y in range(a[1],b[1]+1):
                for X in range(a[0],b[0]+1):
                    game[Y-minimum[1]][X-minimum[0]]="#"

def p1(inp):
    minimum, maximum=get_lows_n_highs(inp)
    difference=[a-b for a,b in zip(maximum,minimum)]

    game=build_walls(
        inp,
        [["." for x  in range(difference[0]+1)] for y in range(difference[1]+1)],
        minimum
    )
    
    sand_blocks=0
    infinite=False
    while not infinite:
        sc=(500-minimum[0],0)
        sand_is_still=False
        
        while not sand_is_still:
            placed=False
            for x,y in [[0,1],[-1,1],[1,1]]:
                if 0<=(sc[0]+x)<len(game[0]) and 0<=(sc[1]+y)<len(game):
                    if game[sc[1]+y][sc[0]+x]==".":
                        new=[sc[0]+x,sc[1]+y]
                        
                        game[sc[1]][sc[0]]="."
                        game[new[1]][new[0]]="o"
                        
                        sc=new; placed=True
                        break
                else: return sand_blocks
            sand_is_still=not placed
        sand_blocks+=1
  
def p2(inp):
    minimum, maximum=get_lows_n_highs(inp)
    maximum=[maximum[0],maximum[1]+2]
    difference=[a-b for a,b in zip(maximum,minimum)]
    
    game=build_walls(
        inp,
        [["#" if difference[1]==y else "." for x  in range(difference[0]+1)] for y in range(difference[1]+1)],
        minimum
    )
    
    sc=1; sc_before=2
    starting_x=500
    
    sand_blocks=0
    while not sc==sc_before:
        sc=(starting_x-minimum[0],0)
        sand_is_still=False
        
        sc_before=sc
        while not sand_is_still:
            placed=False
            for x,y in [[0,1],[-1,1],[1,1]]:
                if not 0<=(sc[0]+x)<len(game[0]):
                    sc[0]+=1; starting_x+=1
                    for w,_ in enumerate(game): 
                        game[w].insert(0,"." if not w==len(game)-1 else "#")
                        game[w].append("." if not w==len(game)-1 else "#")
                
                if game[sc[1]+y][sc[0]+x]==".":
                    new=[sc[0]+x,sc[1]+y]
                    
                    game[sc[1]][sc[0]]="."
                    game[new[1]][new[0]]="o"
                    
                    sc=new; placed=True
                    break
            sand_is_still=not placed      
        sand_blocks+=1
    return sand_blocks