class Solution {
public:
  vector<vector<int>> subsets(vector<int> &nums) {
    int n = nums.size();
    vector<vector<int>> res;
    res.reserve(1 << n);
    int masksCount = 1 << n;

    for (int mask = 0; mask < masksCount; mask++) {
      vector<int> tmp;
      for (int i = 0; i < n; i++) {
        if (mask & (1 << i)) {
          tmp.push_back(nums[i]);
        }
      }
      res.push_back(tmp);
    }

    return res;
  }
};