#include <unordered_set>
#include <vector>

using std::unordered_set;
using std::vector;

class Solution {
public:
  bool checkIfExist(vector<int> &arr) {
    unordered_set<int> seen;
    seen.reserve(arr.size());

    for (int num : arr) {
      if (seen.count(num * 2) || (num % 2 == 0 && seen.count(num / 2))) {
        return true;
      }

      seen.insert(num);
    }

    return false;
  }
};