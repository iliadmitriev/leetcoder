#include <string>
#include <vector>

using std::vector, std::string;

/*

Run length is a subarray of consecutive identical characters

SegmentTree
 - pre: run length starting from the left boundary of the segrment
 - suf: run length ending at the right boundary of the segment
 - best: lenght of the longest run length anywhere inside the segment

             Parent
        ┌───────────────┐
        │               │
      Left            Right
   ┌───────┐        ┌───────┐
   │       │        │       │
   suffix  │        │ prefix│
   └───────┘        └───────┘
          \          /
           \        /
            boundary

Update the current node:
 - the prefix is initialized as prefix of the left child
 - the suffix is initialized as suffix of the right child
 - the best of the currenct node is calculated as max between left and right
   child's best
 - if characters mid and mid + 1 are the same (the indentical character segment
    is crossing the mid boundary):
  + get the lenght of the left and right child
  + check if the left child prefix characters are identical: can be attached to
    the right
  + check if the right child prefix characters are identical: can be attached to
    the left
  + best of the current node refined by updated by the prefix of the left node
    and the prefix of the right node

build process:
- size (2 << log(n), n << 2)
- leaf node: l==r => pre=1, suf=1, best=1 (base case)
-

*/

class SegmentTree {
private:
    int _n;
    int _size;
    vector<int> _pre, _suf, _best;
    string _ch;

    void _build(int node, int l, int r) {
        if (l == r) {
            _pre[node] = 1;
            _suf[node] = 1;
            _best[node] = 1;
            return;
        }

        int left = node << 1;
        int right = node << 1 | 1;
        int mid = (l + r) >> 1;

        _build(left, l, mid);
        _build(right, mid + 1, r);

        _updateNode(node, l, r);
    }

    // leaf node to update, [l, r] - range, i - update char position
    // O(1)
    void _updateNode(int node, int l, int r) {
        int left = node << 1;
        int right = node << 1 | 1;

        // init
        _pre[node] = _pre[left];
        _suf[node] = _suf[right];
        _best[node] = std::max(_best[left], _best[right]);

        // refine if the left and the right parts can be joined
        // (both have adjacent identical symbols in the middle)
        int mid = (l + r) >> 1;
        if (_ch[mid] == _ch[mid + 1]) {
            int lenL = mid - l + 1;
            int lenR = r - mid;

            // the whole left part consist of identical symbols
            if (lenL == _pre[left]) {
                _pre[node] = _pre[left] + _pre[right];
            }

            if (lenR == _suf[right]) {
                _suf[node] = _suf[left] + _suf[right];
            }

            _best[node] = std::max(_best[node], _suf[left] + _pre[right]);
        }
    }

    // update downwards: root to leaf
    // O(log n)
    void _update(int node, int l, int r, int i) {
        // no need to update single symbol is always equal to 1
        if (l == r) {
            return;
        }

        // which part to update
        int mid = (l + r) >> 1;
        if (i <= mid) {
            _update(node << 1, l, mid, i);
        } else {
            _update(node << 1 | 1, mid + 1, r, i);
        }

        _updateNode(node, l, r);
    }

public:
    SegmentTree(const string& s)
        : _n(s.size()), _size(_n << 2), _pre(_size), _suf(_size), _best(_size),
          _ch(s) {
        _build(1, 0, _n - 1);
    }

    inline void updateCharAt(char c, int pos) {
        _ch[pos] = c;
        _update(1, 0, _n - 1, pos);
    }

    inline int best() { return _best[1]; }
};

class Solution {
public:
    vector<int> longestRepeating(string s, string queryCharacters,
                                 vector<int>& queryIndices) {

        const int k = queryIndices.size();
        vector<int> res(k, 0);
        SegmentTree tree(s);

        for (int i = 0; i < k; i++) {
          tree.updateCharAt(queryCharacters[i], queryIndices[i]);
          res[i] = tree.best();
        }

        return res;
    }
};