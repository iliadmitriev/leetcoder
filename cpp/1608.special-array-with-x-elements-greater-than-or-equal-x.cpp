
class Solution {
public:
  int specialArray(vector<int> &nums) {
    int n = nums.size();
    vector<int> cnt(n + 1, 0);

    for (int num : nums) {
      int idx = min(num, n);
      cnt[idx]++;
    }

    int total = 0;
    for (int i = n; i >= 0; i--) {
      total += cnt[i];
      if (total == i) {
        return i;
      }
    }

    return -1;
  }
};