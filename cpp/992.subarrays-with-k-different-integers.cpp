class Solution {
public:
  int subarraysWithKDistinct(vector<int> &nums, int k) {
    int res = 0;
    unordered_map<int, int> freq;
    int i = 0, j = 0;

    for (int r = 0; r < nums.size(); r++) {
      freq[nums[r]]++;

      while (freq.size() > k) {
        freq[nums[j]]--;
        if (freq[nums[j]] == 0)
          freq.erase(nums[j]);
        i = ++j;
      }

      while (freq[nums[j]] > 1) {
        freq[nums[j]]--;
        j++;
      }

      if (freq.size() == k)
        res += j - i + 1;
    }
    return res;
  }
};