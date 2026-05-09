
class Solution {
public:
  int findKthNumber(int n, int k) {
    int i = 1;   // step counter (position pointer in lexicographical tree)
    int cur = 1; // current pointer

    while (i < k) {
      int numberOfChild = countChildNodes(cur, n);

      // check if current node does not include the solution
      if (i + numberOfChild <= k) {
        // then go to the right sibling node
        // skipping all the children nodes (fast forward all steps in one
        // iteration)
        cur++;
        i += numberOfChild;
      } else {
        // otherwise go down to the next level with one step
        cur *= 10;
        i++;
      }
    }

    return cur;
  }

private:
  int countChildNodes(long cur, int limit) {
    int count = 0;
    // right brother or current node is a bound
    // limit = 1361
    // 1 .. 2                  => 1
    // 10 .. 20                => 10
    // 100 ... 200             => 100
    // 1000 ... 1361 ... 2000  => 362
    // cur  ... limit ... bound
    long bound = cur + 1;

    while (cur <= limit) {
      // count number of nodes in current level (inclusive)
      count += bound - cur;

      // move to the next level
      cur *= 10;
      bound *= 10;

      // bound to a not inclusive (+1) limit
      if (bound - 1 > limit) {
        bound = limit + 1;
      }
    }

    return count;
  }
};