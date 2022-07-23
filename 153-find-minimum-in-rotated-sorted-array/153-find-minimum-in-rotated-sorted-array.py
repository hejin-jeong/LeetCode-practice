class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        binary search
        
        """
        if len(nums) == 1 or nums[0] < nums[len(nums)-1]:
            return nums[0]
        
        # binary search
        l = 0
        h = len(nums)-1
        while l < h:
            mid = (l+h)//2
            
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            
            if nums[l] < nums[mid]:
                l = mid+1
            else:
                h = mid-1