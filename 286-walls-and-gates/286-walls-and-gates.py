class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return 
        
        r, c= len(rooms), len(rooms[0])
        
        for i in xrange(r):
            for j in xrange(c):
                
                # Start from the gate
                if rooms[i][j] == 0:
                    queue = collections.deque([])
                    
                    # First, store location with distance 1 from each gate
                    queue.append((i+1, j, 1)); queue.append((i-1, j, 1))
                    queue.append((i, j+1, 1)); queue.append((i, j-1, 1))
                    visited = set()
                    
                    while queue:
                        
                        # Pop and add its neighbors
                        x, y, val = queue.popleft()
                        
                        # If the distance 1 location is outside the grid, walls, or visitied
                        # just pop the location and move on to the next gate
                        if x < 0 or x >= r or y < 0 or y >= c or rooms[x][y] in [0, -1] or (x, y) in visited:
                            continue
                        visited.add((x, y))
                        
                        # It's originally 2^31 so min will be the distance
                        rooms[x][y] = min(rooms[x][y], val)
                        
                        # Add location with distance 1 from distance 1, which means distance 2 from gates
                        # and repeat the while loop for checking their validity
                        queue.append((x+1, y, val+1)); queue.append((x-1, y, val+1))
                        queue.append((x, y+1, val+1)); queue.append((x, y-1, val+1))