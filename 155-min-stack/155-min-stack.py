class MinStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append((val, val))
        else:
            prev, min_val = self.stack[len(self.stack)-1]
            if val < min_val:
                self.stack.append((val, val))
            else:
                self.stack.append((val, min_val))
        
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        val, min_val = self.stack[len(self.stack)-1]
        return val
        

    def getMin(self):
        """
        :rtype: int
        """
        val, min_val = self.stack[len(self.stack)-1]
        return min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()