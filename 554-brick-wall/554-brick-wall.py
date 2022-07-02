class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        
        track the number of gaps -> dict
        return len(wall) - max_gap
        """
        gaps = dict()
        for row in wall:
            count = 0
            for brick in row[:-1]:
                count += brick
                if count in gaps:
                    gaps[count] += 1
                else:
                    gaps[count] = 1
        
        if not gaps:
            max_gap = 0
        else:
            max_gap = max(gaps.values())
        return len(wall) - max_gap