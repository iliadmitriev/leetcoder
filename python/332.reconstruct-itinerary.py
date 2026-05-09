class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    
        adj = defaultdict(list)
        for fr, to in tickets:
            adj[fr].append(to)

        for key in adj.keys():
            adj[key].sort(reverse=True)

        res = []
        stack = ["JFK"]
        while stack:
            des = stack[-1]
            if adj[des]:
                stack.append(adj[des].pop())
            else:
                res.append(stack.pop())

        return res[::-1]