#include <cmath>
#include <string>
#include <unordered_set>
#include <vector>
using std::unordered_set;
using std::vector;
class Solution {
public:
  int longestCommonPrefix(vector<int> &arr1, vector<int> &arr2) {

    unordered_set<int> cache;
    for (int num : arr1) {
      while (num) {
        cache.insert(num);
        num /= 10;
      }
    }

    int maxPrefixLen = 0;

    for (int num : arr2) {
      while (num) {
        if (cache.count(num)) {
          maxPrefixLen =
              std::max(maxPrefixLen, int(std::to_string(num).size()));
          break;
        }

        num /= 10;
      }
    }

    return maxPrefixLen;
  }
};