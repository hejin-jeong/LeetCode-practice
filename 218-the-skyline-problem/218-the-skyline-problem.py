from collections import defaultdict
class Solution:
    def getSkyline(self, buildings):
        coords = []
        hashmap = defaultdict(list)
        for building in buildings:
            hashmap[(building[0], 0)].append(building[2])
            hashmap[(building[1], 1)].append(building[2])
        
        reordered = sorted(list(hashmap.items()))
        print(reordered)
        
        stack = []
        heapq.heappush(stack, 0)
        out = []
        # pre = 3 |  post = 0 | stack = [0]
        for item, _ in reordered:
            pre_height = heapq.nlargest(1, stack)[0]
            if item[1] == 0:
                if len(hashmap[item]) == 1:
                    cur_height = hashmap[item][0]
                    heapq.heappush(stack, cur_height)
                else:
                    while hashmap[item]:
                        cur_height = hashmap[item].pop()
                        heapq.heappush(stack, cur_height)
            elif item[1] == 1:
                if len(hashmap[item]) == 1:
                    cur_height = hashmap[item][0]
                    stack.remove(cur_height)
                else:
                    while hashmap[item]:
                        cur_height = hashmap[item].pop()
                        stack.remove(cur_height)
            post_height = heapq.nlargest(1, stack)[0]
            if pre_height != post_height:
                out.append((item[0], post_height))
        return out