class BinaryIndexTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.tree = [0] * (n + 1)

    @staticmethod
    def lowbit(i: int) -> int:
        return i & -i

    def update(self, i: int, v: int) -> None:
        while i <= self.n:
            self.tree[i] ^= v
            i += self.lowbit(i)

    def query(self, i: int) -> int:
        res = 0

        while i:
            res ^= self.tree[i]
            i -= self.lowbit(i)

        return res

    def update_range(self, l: int, r: int, v: int) -> None:
        self.update(l, v)
        self.update(r + 1, v)

class BinaryUpliftTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.LOG = n.bit_length()
        self.fa = [[0] * self.LOG for _ in range(n)]
        self.l = [0] * n # l[v] position of node v within preorder traversal
        self.r = [0] * n # r[v] position of node v within postorder traversal
        self.dep = [0] * n # depth of i-th vertice
        self.t = 0 # vertice index


    def build(self, g: list[list[int]]):

        def dfs(u: int, p: int = 0):
            self.t += 1

            self.l[u] = self.t
            self.fa[u][0] = p
            
            for v in g[u]:
                if v == p:
                    continue # skip parent node
                self.dep[v] = self.dep[u] + 1
                dfs(v, u)

            self.r[u] = self.t

        dfs(0)

        for j in range(1, self.LOG):
            for i in range(self.n):
                prev = self.fa[i][j - 1]
                self.fa[i][j] = self.fa[prev][j - 1]

    def lca(self, u: int, v: int) -> int:
        if self.dep[u] < self.dep[v]:
            u, v = v, u
        
        diff = self.dep[u] - self.dep[v]
        for i in range(self.LOG):
            if (diff >> i) & 1:
                u = self.fa[u][i]
        
        if u == v:
            return u
        
        for i in range(self.LOG - 1, -1, -1):
            if self.fa[u][i] != self.fa[v][i]:
                u = self.fa[u][i]
                v = self.fa[v][i]
        return self.fa[u][0]

    def left(self) -> list[int]:
        return self.l

    def right(self) -> list[int]:
        return self.r



class Solution:
    def palindromePath(
        self, n: int, edges: list[list[int]], s: str, queries: list[str]
    ) -> list[bool]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def char_bit(ch: str) -> int:
            return 1 << (ord(ch) - ord("a"))

        res = []
        s = list(s)

        # binary index tree
        bit = BinaryIndexTree(n + 1)
        
        # binary uplift tree
        but = BinaryUpliftTree(n)
        but.build(g)
        l, r = but.left(), but.right()

        for i, ch in enumerate(s):
            bit.update_range(l[i], r[i], char_bit(ch))

        for q in queries:
            op, *args = q.split()

            if op == "update":
                u, ch = int(args[0]), args[1]
                bit.update_range(l[u], r[u], char_bit(ch) ^ char_bit(s[u]))
                s[u] = ch
            else:
                u, v = int(args[0]), int(args[1])
                w = but.lca(u, v)
                mask = bit.query(l[u]) ^ bit.query(l[v]) ^ char_bit(s[w])
                res.append(mask & (mask - 1) == 0)

        return res
