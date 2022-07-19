class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        1. Create bucket(queue) for rotten oranges
        2. while queue, Dequeque it, change to 0, if have neighbors, get neighbors, enqueue them, count +=1
        3. loop the grid, if item != 0, return -1, otherwise minute
        """
        from collections import deque
        
        rotten = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    rotten.append((i,j))
        
        minute = 0
        temp = deque()
        while rotten:
            
            row, col = rotten.popleft()
            if row+1 < len(grid) and grid[row+1][col] == 1:
                grid[row+1][col] = 2
                temp.append((row+1,col))
            if col+1 < len(grid[row]) and grid[row][col+1] == 1:
                grid[row][col+1] = 2
                temp.append((row,col+1))
            if row-1 > -1 and grid[row-1][col] == 1:
                grid[row-1][col] = 2
                temp.append((row-1,col))
            if col-1 > -1 and grid[row][col-1] == 1:
                grid[row][col-1] = 2
                temp.append((row,col-1))
                
            if not rotten:
                if temp:
                    rotten = temp
                    temp = deque()
                    minute += 1
                    
        for k in range(len(grid)):
            for p in range(len(grid[k])):
                if grid[k][p] == 1:
                    return -1

        return minute
        