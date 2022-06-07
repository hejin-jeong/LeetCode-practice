class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cycle = 0
        while n != 1 and cycle < 100:
            k = len(str(n))
            s = 0
            count = 0
            while count < k:
                s += (n%10)**2
                n = n//10
                count += 1
            n = s   
            cycle += 1
        
        if n == 1:
            return True
        return False