#include <numeric>
#include <vector>

using std::vector;

class Solution {
public:
  int maxSumDivThree(vector<int> &nums) {
    int total = std::accumulate(nums.begin(), nums.end(), 0);
    int rem = total % 3;

    if (rem == 0) {
      return total;
    }

    const int INF = 1e9;
    int a1 = INF, b1 = INF; // two smallest numbers with remainder 1
    int a2 = INF, b2 = INF; // two smallest numbers with remainder 2

    for (int num : nums) {
      if (num % 3 == 1) {
        if (num <= a1) {
          b1 = a1;
          a1 = num;
        } else if (num < b1) {
          b1 = num;
        }
      } else if (num % 3 == 2) {
        if (num <= a2) {
          b2 = a2;
          a2 = num;
        } else if (num < b2) {
          b2 = num;
        }
      }
    }

    if (rem == 1) {
      return total - std::min(a1, a2 + b2);
    } else { // rem == 2
      return total - std::min(a1 + b1, a2);
    }
  }
};