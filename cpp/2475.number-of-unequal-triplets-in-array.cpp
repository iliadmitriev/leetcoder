#include <unordered_map>
#include <vector>

using std::unordered_map;
using std::vector;

class Solution {
private:
  int comb(int n, int k) {
    if (n < k) {
      return 0;
    }

    if (n < 2 * k) {
      k = n - k;
    }

    int res = 1;
    for (int d = 1; d <= k; d++) {
      res *= n--;
      res /= d;
    }
    return res;
  }

public:
  int unequalTriplets(vector<int> &nums) {
    unordered_map<int, int> freq;
    for (int num : nums) {
      freq[num]++;
    }

    int n = nums.size();
    int totalCombs = comb(n, 3);

    for (auto [_, v] : freq) {
      if (v < 2) {
        continue;
      }
      int tree = comb(v, 3);
      int two = (n - v) * comb(v, 2);
      totalCombs -= two + tree;
    }

    return totalCombs;
  }
};