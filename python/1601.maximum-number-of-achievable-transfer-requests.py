class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        graph = defaultdict(set)
        result = 0
        
        # build graph[from] -> (to, request index)
        # add all the loops to result
        for i, (from_, to) in enumerate(requests):
            if from_ == to:
                result += 1
            else:
                graph[from_].add((to, i))

        # find all unique cycles in transfer list
        # a cycle is a tuple of sorted transfer indexes
        cycles = set()
        def dfs(from_, request_path, building_path):
            for to, i in graph[from_]:
                if to in building_path:
                    # find where current found cycle starts
                    start = building_path.index(to)
                    cycles.add(tuple(sorted(request_path[start:] + [i])))
                else:
                    dfs(to, request_path + [i], building_path + [to])

        for i in range(n):
            dfs(i, [], [i])

        # convert transfer cycles to list
        # and make transfer indexes unique
        cycles = [set(x) for x in cycles]

        # to avoid duplications in transfer list
        # we need to find all the unique combination of sets
        def backtrack(j, current):
            max_requests = len(current)
            for k in range(j, len(cycles)):
                # if two cycles have no intersertion
                # size of a unioun equals to sum of sizes of sets
                joined = current | cycles[k]
                if len(joined) == len(current) + len(cycles[k]):
                    # then join this two cycles
                    max_requests = max(backtrack(k + 1, joined), max_requests)
            return max_requests

        return result + backtrack(0, set())