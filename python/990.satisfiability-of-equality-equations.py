class UnionFind:
    def __init__(self):
        self.parents = dict()
    
    def find(self, node):
        """If node doesn't have parent return it.
        Otherwise find and return it's parent.
        """
        if self.parents.get(node, node) != node:
            self.parents[node] = self.find(self.parents.get(node, node))
        
        return self.parents.get(node, node)
    
    def union(self, node1, node2):
        """Join nodes."""
        p1, p2 = self.find(node1), self.find(node2)
        if p1 != p2:
            self.parents[p1] = p2
            
    def is_connected(self, node1, node2) -> bool:
        p1, p2 = self.find(node1), self.find(node2)
        return p1 == p2
        

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        pos_eq, neg_eq = [], []
        for eq in equations:
            a, b = eq[0], eq[-1]
            if eq[1] == '=':
                pos_eq.append((a, b))
            else:
                neg_eq.append((a, b))
        
        uf = UnionFind()  
        for a, b in pos_eq:
            uf.union(a, b)
            
        for a, b in neg_eq:
            if uf.is_connected(a, b):
                return False
                
        return True