class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = [0]*(n+1)
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        pp = 1
        p = 2
        
        for i in range(3,n+1):
            t = p + pp
            pp = p
            p = t
            
        return t
    
    
    
        
#         steps = [0]*(n+1)
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
        
#         steps[1] = 1
#         steps[2] = 2
        
#         for i in range(3,n+1):
#             steps[i] = steps[i-1] + steps[i-2]
            
#         return steps[n]
        
        
        # Below solutions are O(2^n)
        
        # if n == 0:
        #     return 1
        # elif n < 0:
        #     return 0
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
            
        
        
        
#         def helper(step):
#             if step == n:
#                 return 1
#             if step > n:
#                 return 0
            
#             one = helper(step+1)
#             two = helper(step+2)
            
#             return one + two
        
        
#         return helper(0)
        