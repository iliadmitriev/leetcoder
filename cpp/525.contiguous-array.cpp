class Solution {
public:
  int findMaxLength(vector<int> &nums) {
    int cnt = 0;
    int res = 0;

    unordered_map<int, int> dp;
    dp[0] = -1;

    for (int i = 0; i < nums.size(); ++i) {
      cnt += nums[i] ? 1 : -1;

      if (dp.find(cnt) != dp.end()) {
        res = max(res, i - dp[cnt]);
      } else {
        dp[cnt] = i;
      }
    }

    return res;
  }
};