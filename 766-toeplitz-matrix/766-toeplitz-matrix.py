class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row = 0
        while row < len(matrix)-1:
            # first row: iterate every element and increment to the pattern
            # from second row: just to the first element and move on to the next row
            col = 0
            if row == 0:
                r = row
                while r < len(matrix) and col < len(matrix[0])-1:
                    i,j = r+1,col+1
                    while i < len(matrix) and j <len(matrix[0]):
                        if matrix[r][col] != matrix[i][j]:
                            return False
                        i += 1
                        j += 1
                    col += 1
            
            else:
                check = matrix[row][col]
                i,j = row+1,col+1
                while i < len(matrix) and j <len(matrix[0]):
                    if check != matrix[i][j]:
                        return False
                    i += 1
                    j += 1
                
                
                    
            row += 1
            
        return True
                
        