class Solution {
public:
  int maxFrequencyElements(vector<int> &nums) {
    vector<int> cnt(101);
    for (auto num : nums) {
      cnt[num]++;
    }
    int m = cnt[max_element(cnt.begin(), cnt.end()) - cnt.begin()];
    int res = 0;
    for (auto c : cnt) {
      if (c == m) {
        res += c;
      }
    }
    return res;
  }
};