class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if len(rooms) <= 1:
            return True

        visited = [False]*len(rooms)

        def dfs(rooms, key):
            if visited[key]:
                return
            else:
                visited[key] = True

            for key in rooms[key]:
                dfs(rooms, key)

        dfs(rooms, 0)

        for room in visited:
            if room == False:
                return False

        return True