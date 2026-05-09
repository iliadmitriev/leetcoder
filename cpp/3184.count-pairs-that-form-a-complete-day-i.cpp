#include <cassert>
#include <vector>

using std::vector;

class Solution {

private:
  long long combinations(int n, int r) {
    if (r > n)
      return 0;
    if (r > n / 2)
      r = n - r; // Because C(n, r) == C(n, n - r)
    long long ans = 1;
    int i;

    for (i = 1; i <= r; i++) {
      ans *= n - r + i;
      ans /= i;
    }

    return ans;
  }

public:
  int countCompleteDayPairs(vector<int> &hours) {
    vector<int> counter(24, 0);

    for (int h : hours) {
      counter[h % 24]++;
    }

    int h0 = combinations(counter[0], 2);
    int h12 = combinations(counter[12], 2);
    int other = 0;

    for (int h = 1; h < 12; h++) {
      other += counter[h] * counter[24 - h];
    }

    return h0 + h12 + other;
  }
};