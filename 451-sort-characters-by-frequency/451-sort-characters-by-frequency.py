import heapq
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        Hashmap & Maxheap
        """
        res = ""
        freq = {}
        for cha in s:
            if cha not in freq:
                freq[cha] = 1
            else:
                freq[cha] += 1
        
        heap = [(-(freq[char]), char) for char in freq]
        heapq.heapify(heap)
        
        while heap:
            freq, cha = heapq.heappop(heap)
            res += cha*(-freq)
        return res
        
        
#         # Build heap
# 	heap = [(-v, k) for k, v in cnt.items()]
# 	heapq.heapify(heap)
	
# 	# Build string
# 	res = []
# 	while heap:
# 		v, k = heapq.heappop(heap)
# 		res += [k] * -v
# 	return ''.join(res)