class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        
        while looping the intervals, add start and end point of each interval to the stack.
        if new start point is less than or equal to the stack[-1], continue. 
        if new end point is less than stack[-1], continue.
        else: stack.pop() and add this new end to the stack.
        return result
        """
        intervals.sort()
        stack = []
        for interval in intervals:
            if not stack:
                stack.append(interval[0])
                stack.append(interval[1])
            else:
                if interval[0] <= stack[-1]:
                    if interval[1] > stack[-1]:
                        stack.pop()
                        stack.append(interval[1])
                        
                else:
                    stack.append(interval[0])
                    stack.append(interval[1])
        
        result = []
        i = 0
        while i < len(stack):
            result.append([stack[i],stack[i+1]])
            i += 2
            
        return result
                    