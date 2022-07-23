class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        interval_to_merge = newInterval
        flag = True
        i = 0
        while i < len(intervals):
            curr_interval = intervals[i]
            if curr_interval[1] < interval_to_merge[0]:
                result.append(curr_interval)
            elif interval_to_merge[1] < curr_interval[0]:
                break

            else:
                interval_to_merge = [min(curr_interval[0], interval_to_merge[0]), max(curr_interval[1], interval_to_merge[1])]
            i += 1

        result.append(interval_to_merge)
        
        if i < len(intervals):
            while i < len(intervals):
                result.append(intervals[i])
                i += 1
        return result