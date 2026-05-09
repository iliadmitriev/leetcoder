#include <vector>
using std::vector;

class Solution {
public:
  vector<int> distinctDifferenceArray(vector<int> &nums) {
    vector<int> res;
    vector<int> prefix(51, 0), suffix(51, 0);

    int prefixCount = 0, suffixCount = 0;
    for (int num : nums) {
      suffix[num]++;
      if (suffix[num] == 1)
        suffixCount++;
    }

    for (int num : nums) {
      prefix[num]++;
      if (prefix[num] == 1)
        prefixCount++;

      suffix[num]--;
      if (suffix[num] == 0)
        suffixCount--;

      res.push_back(prefixCount - suffixCount);
    }

    return res;
  }
};