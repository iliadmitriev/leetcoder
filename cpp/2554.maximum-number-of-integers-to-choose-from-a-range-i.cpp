#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
  int maxCount(vector<int> &banned, int n, int maxSum) {
    int total = 0;
    int count = 0;

    int maxInt = std::max(*std::max_element(banned.begin(), banned.end()), n);
    vector<bool> bannedSet(maxInt + 1, false);
    for (int b : banned) {
      bannedSet[b] = true;
    }

    for (int i = 1; i <= n && total + i <= maxSum; i++) {
      if (bannedSet[i]) {
        continue;
      }

      total += i;
      count++;
    }

    return count;
  }
};