class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        
        If cycle,then false
        DFS
        """
        if not prerequisites:
            return True

        from collections import defaultdict
        graph = defaultdict(list)
        
        for value, key in prerequisites:
            if key == value:
                return False
            graph[key].append(value)
        
#         visited = set()
        
#         def helper(v, visited):
#             visited.add(v)
            
#             if graph[v] in graph:
#                 if graph[v] not in visited:
#                     helper(graph[v], visited)
#                 else:
#                     return False
                
#         for v in graph:
#             if v not in visited:
#                 helper(v, visited)
#             else:
#                 return False
            
#         return True




            # Each vertex can have 3 different states:
            # state 0   : vertex is not visited. It's a default state.
            # state -1  : vertex is being processed. Either all of its descendants
            #             are not processed or it's still in the function call stack.
            # state 1   : vertex and all its descendants are processed.
        state = [0] * numCourses

        def hasCycle(v):
            if state[v] == 1:
                # This vertex is processed so we pass.
                return False
            if state[v] == -1:
                # This vertex is being processed and it means we have a cycle.
                return True

            # Set state to -1
            state[v] = -1

            for i in graph[v]:
                if hasCycle(i):
                    return True

            state[v] = 1
            return False

        # we traverse each vertex using DFS, if we find a cycle, stop and return
        for v in range(numCourses):
            if hasCycle(v):
                return False

        return True

            