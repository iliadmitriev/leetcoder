#include <algorithm>
#include <vector>
using std::vector;

class Solution {
private:
  inline int pop_count(int num) { return __builtin_popcount(num); }

public:
  bool canSortArray(vector<int> &nums) {
    int n = nums.size();

    vector<int> sorted;

    int j = 0, bits = pop_count(nums[0]);
    for (int i = 0; i < n; i++) {
      if (bits != pop_count(nums[i])) {
        vector<int> part(nums.begin() + j, nums.begin() + i);
        std::sort(part.begin(), part.end());

        sorted.insert(sorted.end(), part.begin(), part.end());

        bits = pop_count(nums[i]);
        j = i;
      }
    }

    if (j < n) {
      vector<int> part(nums.begin() + j, nums.end());
      std::sort(part.begin(), part.end());

      sorted.insert(sorted.end(), part.begin(), part.end());
    }

    std::sort(nums.begin(), nums.end());

    for (int i = 0; i < n; i++) {
      if (sorted[i] != nums[i])
        return false;
    }

    return true;
  }
};