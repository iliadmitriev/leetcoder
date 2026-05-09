#include <unordered_set>
#include <vector>

using std::unordered_set;
using std::vector;

class Solution {
public:
  int longestConsecutive(vector<int> &nums) {
    unordered_set<int> numsSet(nums.begin(), nums.end());
    int maxLen = 0;

    for (int num : numsSet) {
      // skip if it's not a start of a sequence
      if (numsSet.count(num - 1)) {
        continue;
      }

      // find all consecutive numbers for a current sequence
      int seqLen = 1;
      while (numsSet.count(num + seqLen)) {
        seqLen++;
      }

      maxLen = std::max(maxLen, seqLen);

      // if's current sequence is longer than a half of all array length
      // then is's impossible to find another greater sequence in this array
      if (maxLen > nums.size() / 2) {
        break;
      }
    }

    return maxLen;
  }
};