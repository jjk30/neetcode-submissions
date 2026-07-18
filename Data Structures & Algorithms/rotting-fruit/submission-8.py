from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        fresh=0
        spread=0
        direct=[(1,0),(-1,0),(0,1),(0,-1)]
        q=deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    fresh+=1
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in direct:
                     nr=r+dr
                     nc=c+dc
                     if nr<0 or nr>=row or nc<0 or nc>=col:
                        continue
                     if grid[nr][nc]!=1:
                        continue
                     grid[nr][nc]=2
                     fresh-=1
                     q.append((nr,nc))
            spread+=1
        return spread if fresh==0 else -1

        
        