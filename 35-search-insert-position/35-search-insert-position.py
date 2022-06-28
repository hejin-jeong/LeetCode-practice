class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        cur = 0
        while cur < len(nums):
            if nums[cur] == target or nums[cur] > target:
                return cur
            
            cur += 1
            
        return cur
        