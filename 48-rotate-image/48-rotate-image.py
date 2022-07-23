class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        '''
        M = matrix
        n = len(M)
        depth = n // 2
        for i in range(depth):
            rlen, opp = n - 2 * i - 1, n - 1 - i
            for j in range(rlen):
                temp = M[i][i+j]
                M[i][i+j] = M[opp-j][i]
                M[opp-j][i] = M[opp][opp-j]
                M[opp][opp-j] = M[i+j][opp]
                M[i+j][opp] = temp
                
        '''  
        '''
        for i in range(0,len(matrix)//2):
        for j in range(i,len(matrix)-2-i):
            temp = matrix[i][j]
            #rotate
            matrix[i][j] = matrix[len(matrix)-1-j][i]
            matrix[len(matrix)-1-j][i] = matrix[len(matrix)-1-i][len(matrix)-1-j]
            maxtrix[len(matrix)-1-i][row] = matrix[j][len(matrix)-1-i]
            matrix[j][len(matrix)-1-i] = temp
    
    #return matrix
    '''

        # reverse
        l = 0
        r = len(matrix) -1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        # transpose 
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]