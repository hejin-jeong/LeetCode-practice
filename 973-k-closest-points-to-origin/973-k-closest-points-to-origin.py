class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        
        create a min heap that has size of k
        loop through the points array and push each point to the min heap based on its distance
        """
        import heapq
        
        heap = []
        for point in points:
            dis = point[0]**2 + point[1]**2
            heapq.heappush(heap, (-dis, point))
            
            if len(heap) > k:
                heapq.heappop(heap)
                
                
        return [point for dis,point in heap]
        
        