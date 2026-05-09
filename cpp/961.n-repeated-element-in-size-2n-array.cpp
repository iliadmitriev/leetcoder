#include <unordered_map>
#include <vector>

using std::unordered_map;
using std::vector;

class Solution {
public:
  int repeatedNTimes(vector<int> &nums) {
    unordered_map<int, int> counter;
    for (int num : nums) {
      counter[num]++;

      if (counter[num] > 1) {
        return num;
      }
    }

    return -1;
  }
};