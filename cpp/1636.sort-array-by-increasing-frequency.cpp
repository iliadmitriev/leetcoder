#include <algorithm>
#include <unordered_map>
#include <vector>

using std::sort;
using std::unordered_map;
using std::vector;

class Solution {
public:
  vector<int> frequencySort(vector<int> &nums) {
    unordered_map<int, int> freq;
    for (int num : nums) {
      ++freq[num];
    }

    sort(nums.begin(), nums.end(), [&freq](int a, int b) {
      return freq[a] < freq[b] || (freq[a] == freq[b] && a > b);
    });

    return nums;
  }
};