#include <vector>
using std::vector;

class Solution {
private:
  long long counter(int a, int b) {
    long long total = 0;

    int prev = 1;
    int cur = 0;
    int left, right;
    for (int d = 1; prev <= b; d++) {
      cur = prev * 4;
      left = std::max(prev, a);
      right = std::min(b, cur - 1);

      if (left <= right) {
        total += long(right - left + 1) * d;
      }

      prev = cur;
    }

    return (total + 1) / 2;
  }

public:
  long long minOperations(vector<vector<int>> &queries) {
    long long total = 0;

    for (const vector<int> &q : queries) {
      total += counter(q[0], q[1]);
    }

    return total;
  }
};