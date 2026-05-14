// @leet start
#include <vector>
using std::vector;

class Solution {
public:
  int minMoves(vector<int> &nums, int limit) {
    const int n = nums.size();
    vector<int> diff(2 * limit + 2, 0);

    for (int i = 0; i < n / 2; i++) {
      int a = nums[i], b = nums[n - 1 - i];

      if (a > b) {
        std::swap(a, b);
      }

      diff[2] += 2;      // worst case both numbers have to be changed
                         // two changes have to be made if a + b < 2)
      diff[a + 1]--;     // one of numbers can be left untoched and another
                         // changed if a < target (leave smallest a untoched,
                         // and set b = target - a, it's garanteed to exist)
      diff[a + b]--;     // no need to change anything (a + b == target)
      diff[a + b + 1]++; // there is one of number should be changed
      diff[b + limit + 1]++; // both numbers should be changed (change one
                             // number is not enough)
    }

    int minMoves = n, moves = 0;

    for (int target = 2; target <= 2 * limit; target++) {
      moves += diff[target];
      minMoves = std::min(minMoves, moves);
    }

    return minMoves;
  }
};
// @leet end
