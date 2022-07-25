class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        Calculate the minimum path sum for each cell in the grid. That said, we can then simply return the minimum sum for the last cell in the grid.
        
        in each cell, update the num to the min path sum
        but only sum from left and up
        """
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    continue
                left = float('inf')
                up = float('inf')
                # from left
                if j > 0:
                    left = grid[i][j-1] 
                # from up
                if i > 0:
                    up = grid[i-1][j]
                grid[i][j] += min(left,up)
                
                
        return grid[len(grid)-1][len(grid[len(grid)-1])-1]