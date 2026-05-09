class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        inorder = [0] * n
        graph = defaultdict(list)
        for a, b in relations:
            inorder[b - 1] += 1
            graph[a - 1].append(b - 1)

        queue = deque([i for i in range(n) if inorder[i] == 0])
        end_time = [0] * n
        for i in queue:
            end_time[i] = time[i]

        while queue:
            node = queue.popleft()

            for child in graph[node]:
                inorder[child] -= 1
                if inorder[child] == 0:
                    queue.append(child)
                end_time[child] = max(end_time[child], end_time[node] + time[child])
                
        return max(end_time)