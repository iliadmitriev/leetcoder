class Solution {
public:
  int maxSubarrayLength(vector<int> &nums, int k) {
    if (k >= nums.size()) {
      return nums.size();
    }

    unordered_map<int, int> freq;
    int ans = 0;
    int i = 0; // left bound

    for (int j = 0; j < nums.size(); ++j) {
      freq[nums[j]]++;

      while (i <= j && freq[nums[j]] > k)
        freq[nums[i++]]--;

      ans = max(ans, j - i + 1);
    }

    return ans;
  }
};