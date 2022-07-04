class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
#         colors = [0]*len(graph)
        
#         for i in range(len(graph)):
#             # if not colored, color it and check neighbor. If not colored, color with different color, otherwise check the color, if same color, return False
#             if colors[i] == 0:
#                 colors[i] = 1
                
        
        
        # Our goal is trying to use two colors to color the graph and see if there are any adjacent nodes having the same color.
# Initialize a color[] array for each node. Here are three states for colors[] array:
# 0: Haven't been colored yet.
# 1: Blue.
# -1: Red.
# For each node,

# If it hasn't been colored, use a color to color it. Then use the other color to color all its adjacent nodes (DFS).
# If it has been colored, check if the current color is the same as the color that is going to be used to color it. (Please forgive my english... Hope you can understand it.)
# DFS Solution:
        colors = [0]*len(graph)
    
    
        def validColor(graph, colors, color, node):
            if colors[node] != 0:
                return colors[node] == color
            colors[node] = color
            for neighbor in graph[node]:
                if not validColor(graph, colors, -color, neighbor):
                    return False
                
            return True
    
        # This graph might be a disconnected graph. So check each unvisited node.
        for i in range(len(graph)):
            if colors[i] == 0 and not validColor(graph, colors, 1, i):
                return False
            
        return True

# BFS Solution:

# class Solution {
#     public boolean isBipartite(int[][] graph) {
#         int len = graph.length;
#         int[] colors = new int[len];
        
#         for (int i = 0; i < len; i++) {
#             if (colors[i] != 0) continue;
#             Queue<Integer> queue = new LinkedList<>();
#             queue.offer(i);
#             colors[i] = 1;   // Blue: 1; Red: -1.
            
#             while (!queue.isEmpty()) {
#                 int cur = queue.poll();
#                 for (int next : graph[cur]) {
#                     if (colors[next] == 0) {          // If this node hasn't been colored;
#                         colors[next] = -colors[cur];  // Color it with a different color;
#                         queue.offer(next);
#                     } else if (colors[next] != -colors[cur]) {   // If it is colored and its color is different, return false;
#                         return false;
#                     }
#                 }
#             }
#         }
        
#         return true;
#     }
# }


# def isBipartite(self, graph):
#         """
#         :type graph: List[List[int]]
#         :rtype: bool
#         """
#         n, colored = len(graph), {}
#         for i in range(n):
#             if i not in colored and graph[i]:
#                 colored[i] = 1
#                 q = collections.deque([i])
#                 while q:
#                     cur = q.popleft()
#                     for nb in graph[cur]:
#                         if nb not in colored:
#                             colored[nb] = -colored[cur]
#                             q.append(nb)
#                         elif colored[nb] == colored[cur]:
#                             return False
#         return True