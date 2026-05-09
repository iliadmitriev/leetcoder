class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # if item doesn't belong to any group assign it an unique group id
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        # print("group", group)

        # init single items dependency graph and indegree of nodes
        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n

        # init item groups dependency graph and indegree of noodes 
        group_graph = [[] for _ in range(m)]
        group_indegree = [0] * m

        # build items and groups graph with their indegrees
        for curr in range(n):
            for prev in beforeItems[curr]:
                # each tuple (prev -> curr) is an edge in items graph
                item_graph[prev].append(curr)
                item_indegree[curr] += 1

                # check if prev and curr belong to different groups
                # then add and edge in the group graph
                if group[curr] != group[prev]:
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1
        
        def topological_sorting(graph: List[List[int]], indegree: List[int]) -> List[int]:
            visited = []
            # add to the starting stack state
            # all the nodes from graph with indegree equal to 0
            stack = [node for node in range(len(graph)) if indegree[node] == 0]
            while stack:
                cur = stack.pop()
                visited.append(cur)
                for adj in graph[cur]:  # iterate all the nodes adjacent to current with an edge
                    indegree[adj] -= 1  # reduce their indegree (the current node is visited)
                    # if adjacent node indegee is equal to 0 (all its predecessor nodes visited)
                    # then add it to stack
                    if indegree[adj] == 0:
                        stack.append(adj)
            # if algorithm is able to visite all the nodes from graph
            # then there is no cycles, and nodes can be sorted topologically
            return visited if len(visited) == len(graph) else []

        # perform topological sort for group and items graph
        item_sorted = topological_sorting(item_graph, item_indegree)
        group_sorted = topological_sorting(group_graph, group_indegree)

        # if it's impossible to sort group or items graph, return earlier empy response
        if not group_sorted or not item_sorted:
            return []

        # print("group_sorted", group_sorted)
        # print("item_sorted", item_sorted)

        # item are sorted regardless of groups
        # combine them to to groups they belong
        item_ordered_by_groups = dict()
        for item in item_sorted:
            item_ordered_by_groups.setdefault(group[item], []).append(item)

        # print(ordered_groups)

        # concatenate all ordered_groups
        result = []
        for group_idx in group_sorted:
            if group_idx in item_ordered_by_groups:
                result += item_ordered_by_groups[group_idx]

        return result