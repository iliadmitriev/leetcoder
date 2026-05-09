class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        seen = {start}
        queue = deque([(start, 0)])
        
        adj_bank = defaultdict(list)
        
        def mutate(gene: str):
            for i in range(0, 8):
                yield gene[:i] + '?' + gene[i + 1:]
        
        for gene in bank:
            for mutation in mutate(gene):
                adj_bank[mutation].append(gene)
        
        while queue:
            gene, depth = queue.popleft()
            
            if gene == end:
                return depth
            
            for mutation in mutate(gene):                
                for next_mutation in adj_bank[mutation]:
                    if next_mutation not in seen:
                        queue.append((next_mutation, depth + 1))
                        seen.add(next_mutation)

        return -1