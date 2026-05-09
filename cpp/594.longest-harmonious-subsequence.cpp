#include <unordered_map>
#include <vector>

using std::vector, std::unordered_map;

class Solution {
public:
  int findLHS(vector<int> &nums) {
    unordered_map<int, int> m;
    int longest = 0;

    for (int num : nums) {
      m[num]++;
    }

    for (auto [k, v] : m) {
      if (m.find(k + 1) != m.end()) {
        longest = std::max(longest, v + m[k + 1]);
      }
    }

    return longest;
  }
};