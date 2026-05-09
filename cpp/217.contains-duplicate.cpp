#include <unordered_set>
#include <vector>

using std::unordered_set;
using std::vector;
class Solution {
public:
  bool containsDuplicate(vector<int> &nums) {
    unordered_set<int> cache;

    for (int num : nums) {
      if (cache.count(num)) {
        return true;
      }

      cache.insert(num);
    }

    return false;
  }
};