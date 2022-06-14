class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
#         # Two pointers
#         res = []
#         f = 0        
#         while f < len(temperatures):
#             s = f + 1
#             count = 1
#             while s < len(temperatures):
#                 if temperatures[f] < temperatures[s]:
#                     res.append(count)
#                     break
#                 s += 1
#                 count += 1
#             if s == len(temperatures):
#                 res.append(0)
                
#             f += 1
                
#         return res


        ans = [0]*len(temperatures)
        stack = []
        for i, v in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < v:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return ans