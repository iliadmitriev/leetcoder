#include <vector>
using std::vector;

class MaxSegmentTree {
private:
  vector<int> tree;
  int size;

public:
  MaxSegmentTree(const vector<int> &nums) {
    int n = nums.size();
    size = 1;

    while (size < n) {
      size <<= 1;
    }

    tree.resize(2 * size);

    for (int i = 0; i < n; i++) {
      tree[size + i] = nums[i];
    }

    for (int i = size - 1; i > 0; i--) {
      tree[i] = std::max(tree[2 * i], tree[2 * i + 1]);
    }
  }

  void update(int i, int x) {
    i += size;
    tree[i] = x;

    i >>= 1;

    while (i) {
      tree[i] = std::max(tree[2 * i], tree[2 * i + 1]);
      i >>= 1;
    }
  }

  int findGt(int x) {

    int i = 1;
    if (x > tree[i]) {
      return -1;
    }

    while (i < size) {
      if (x <= tree[2 * i]) {
        i = 2 * i;
      } else {
        i = 2 * i + 1;
      }
    }

    return i - size;
  }
};

class Solution {
public:
  int numOfUnplacedFruits(vector<int> &fruits, vector<int> &baskets) {
    MaxSegmentTree tree(baskets);

    int count = 0;

    for (int fruit : fruits) {
      int j = tree.findGt(fruit);

      if (j == -1) {
        count++;
        continue;
      }

      tree.update(j, 0);
    }

    return count;
  }
};