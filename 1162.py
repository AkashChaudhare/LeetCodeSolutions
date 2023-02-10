class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        q = collections.deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i,j))
        if not q or len(q) == n*n:
            return -1

        ans =- 1

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while(q):
            size = len(q)
            ans += 1
            while(size):
                size-=1
                i , j = q.popleft()
                for x,y in dirs:
                    x=x+i
                    y=y+j
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        grid[x][y] = 1
                        q.append((x, y)) 
        return ans


            
