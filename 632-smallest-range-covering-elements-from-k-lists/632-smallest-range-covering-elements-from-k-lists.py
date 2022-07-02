class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        
        Beginning from all first items, increase the smallest element among three from each list. 
        Stop when the minimum is the end of the list.
        """
#         pointers = [(each_list[0], list_index, 0) for list_index, each_list in enumerate(nums)]
#         result = [-float('inf'), float('inf')]
        
#         while True:
        
#             small, list_index, ele_index = min(pointers)
#             big, _, _ = max(pointers)

#             if result[1] - result[0] > big - small:
#                 result = [small, big]
                
#             if len(nums[list_index]) == ele_index+1:
#                 return result

#             # increment smallest element, if the range is in the list
#             pointers.remove((small, list_index, ele_index))
#             pointers.append((nums[list_index][ele_index+1], list_index, ele_index+1))

    
    
    
        pq = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(pq)

        ans = -1e9, 1e9
        right = max(row[0] for row in nums)
        while pq:
            left, i, j = heapq.heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if j + 1 == len(nums[i]):
                return ans
            v = nums[i][j+1]
            right = max(right, v)
            heapq.heappush(pq, (v, i, j+1))

