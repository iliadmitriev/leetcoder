
class SegmentTree:
    """Segmet tree with suffix, prefix and best length.
    """
    def __init__(self, s: str) -> None:
        n = len(s)
        self.n = n        
        self.pre = [0] * (n << 2) # x 4
        self.suf = [0] * (n << 2) # x 4
        self.best = [0] * (n << 2) # x 4
        self.s = list(s) # array of chars


        self._build(1, 0, n - 1)

    def _build(self, node: int, l: int, r: int) -> None:
        """Build tree from leaves up to the root."""
        if l == r: # base case 
            self.pre[node] = 1
            self.suf[node] = 1
            self.best[node] = 1
            return

        mid = (l + r) // 2
        left = node << 1
        right = node << 1 | 1

        self._build(left, l, mid)
        self._build(right, mid + 1, r)

        self._update_node(node, l, r)

    def _update(self, node: int, l: int, r: int, i: int) -> None:
        """Update tree leaf i from root to leaf.
        
        node: current node
        l, r: boundaries
        i: updated leaf node
        """
        if l == r:
            return

        mid = (l + r) // 2

        if i <= mid:
            self._update(node << 1, l, mid, i)
        else:
            self._update(node << 1 | 1, mid + 1, r, i)

        self._update_node(node, l, r)

    def _update_node(self, node: int, l: int, r: int) -> None:
        """Update single node with it's childs."""
        left = node << 1
        right = node << 1 | 1

        # base case (left and right parts cannot be connected)
        self.pre[node] = self.pre[left]
        self.suf[node] = self.suf[right]
        self.best[node] = max(self.best[left], self.best[right])

        mid = (l + r) // 2

        # left and right part can be connected
        if self.s[mid] == self.s[mid + 1]:
            len_l = mid - l + 1
            len_r = r - mid

            # the left part is consist only from a single symbol, e.g. "aaaa"
            if len_l == self.pre[left]:
                self.pre[node] = self.pre[left] + self.pre[right]

            # the right part is consist only from a single symbol, e.g. "aaaa"
            if len_r == self.suf[right]:
                self.suf[node] = self.suf[left] + self.suf[right]

            self.best[node] = max(self.best[node], self.suf[left] + self.pre[right])

    def update_char(self, ch: str, i: int) -> None:
        """Update string with character at position i."""
        self.s[i] = ch
        self._update(1, 0, self.n - 1, i)

    def best_segment(self) -> int:
        return self.best[1]

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        tree = SegmentTree(s)
        res = [0] * len(queryCharacters)

        for i, (ch, idx) in enumerate(zip(queryCharacters, queryIndices)):
            tree.update_char(ch, idx)
            res[i] = tree.best_segment()

        return res

        