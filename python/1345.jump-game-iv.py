class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        # build adjacency dict
        adj = defaultdict(list)
        for i, node in enumerate(arr):
            adj[node].append(i)

        seen = [False] * n
        queue = deque([0])
        seen[0] = True
        # result
        step = 0

        while queue:

            for _ in range(len(queue)):
                i = queue.popleft()
                # check if it's a final node
                if i == n - 1:
                    return step
                # step +1
                if i + 1 < n and not seen[i + 1]:
                    seen[i + 1] = True
                    queue.append(i + 1)
                # step -1
                if i - 1 >= 0 and not seen[i - 1]:
                    seen[i - 1] = True
                    queue.append(i - 1)
                # jump arr[i] == arr[j]
                while adj[arr[i]]:
                    j = adj[arr[i]].pop()
                    if j is not seen[j]:
                        seen[j] = True
                        queue.append(j)
            # next round
            step += 1

        return step