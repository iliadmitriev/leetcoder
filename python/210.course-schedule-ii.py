from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        
        Idea:
        
        1) each course is a vertex in a directed unweighted graph G(V, E)
        2) edges are the prerequisite relationship between courses
           pair [a, b] means course b is a prerequisite for a
           edge b -> a
        3) there is a possibility of a cycle in graph.
           clearly if there is a cycle in graph
           then there's no way of finishing all the courses
            
        Using BFS, algorithm of topological sorting look liske this:
        
            1) build adjacency list [[a, b], [e, b]] => {b: [e, a]}
            2) build list of edges count for every vertex
            2) init queue with vertices with 0 count of edges (courses with no prerequisites)
            3) BFS for each node in queue
                a) append node to result
                b) increase node counter
                c) for each neigbour node if decrease it's prerequsites count
                    *) if neigbour has 0 prerequisites add in to queue
                    
            4) return result (reversed) if node counter has reached courses count, othwerwise empty list
            
        Time: O(V + E)
        Space: O(V + E)
        
        """
        adj_list = [list() for _ in range(numCourses)]
        in_order = [0] * numCourses
        for src, dest in prerequisites:
            adj_list[src].append(dest)
            in_order[dest] += 1
            
        topol_sorted = []        
        count = 0
        queue = [u for u in range(numCourses) if in_order[u] == 0]
        
        while queue:
            
            node = queue.pop(0)
            
            count += 1
            topol_sorted.append(node)
            
            for nei in adj_list[node]:
                in_order[nei] -= 1
                if in_order[nei] == 0:
                    queue.append(nei)
            
        return topol_sorted[::-1] if count == numCourses else []
    