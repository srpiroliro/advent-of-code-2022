import collections

with open("input.txt") as f: i = f.readlines()

class Map:
    possible_moves=[[0,1],[0,-1],[-1,0],[1,0]]

    def __init__(self):
        mp=[]

        for o,y in enumerate(i):
            mp.append([])
            for u,x in enumerate(y.strip()):
                if x=="S": 
                    start_point=(u,o)
                    x="a"
                elif x=="E": 
                    end_point=(u,o)
                    x="z"
                mp[o].append(x)

        self.distance = [[0 for _ in row] for row in mp]

        self.map = mp
        self.start_point=start_point
        self.end_point=end_point
    
    def p2(self):
        a_starting_points=[]
        for o,y in enumerate(self.map):
            for u,x in enumerate(y):
                if x=="a": a_starting_points.append((u,o))

        results=[]
        for start in a_starting_points:
            path=self.bfs(self.map, start)
            if path: results.append(len(path)-1)
        return(min(results))

    def p1(self): 
        return len(self.bfs(self.map, self.start_point))-1

    def bfs(self, grid, start):
        width,height=len(grid[0]), len(grid)
        queue=collections.deque([[start]])
        seen=set([start])
        while queue:
            path=queue.popleft()
            x,y=path[-1]
            t=grid[y][x]
            if [x,y]==self.end_point: return path
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0<=x2<width and 0<=y2<height and (x2, y2) not in seen:
                    if ord(grid[y2][x2])-ord(t)<=1:
                        queue.append(path+[(x2,y2)])
                        seen.add((x2,y2))