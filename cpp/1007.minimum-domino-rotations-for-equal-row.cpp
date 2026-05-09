#include <vector>
using std::vector;

class Solution {
public:
  int minDominoRotations(vector<int> &tops, vector<int> &bottoms) {
    const int n = tops.size();
    vector<int> both(7, 0), top(7, 0), bot(7, 0);

    for (int i = 0; i < n; i++) {
      top[tops[i]]++;
      bot[bottoms[i]]++;
      if (tops[i] == bottoms[i]) {
        both[tops[i]]++;
      }
    }

    for (int i = 1; i <= 6; i++) {
      if (top[i] + bot[i] - both[i] == n) {
        return n - std::max(top[i], bot[i]);
      }
    }

    return -1;
  }
};