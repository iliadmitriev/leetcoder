#include <unordered_set>
#include <vector>

using std::vector, std::unordered_set;

class Solution {
private:
  int maxFib(int a, int b, const unordered_set<int> &order) {
    if (!order.count(a + b)) {
      return 0;
    }

    return 1 + maxFib(b, a + b, order);
  }

public:
  int lenLongestFibSubseq(vector<int> &arr) {
    const int N = arr.size();
    unordered_set<int> order(arr.begin(), arr.end());
    int longestFib = 0;

    for (int i = 0; i < N; ++i) {
      for (int j = i + 1; j < N; ++j) {
        longestFib = std::max(longestFib, 2 + maxFib(arr[i], arr[j], order));
      }
    }

    if (longestFib <= 2) {
      return 0;
    }

    return longestFib;
  }
};