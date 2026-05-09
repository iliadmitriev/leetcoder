#include <unordered_map>
#include <vector>

using std::vector, std::unordered_map;

class Solution {
private:
  typedef unordered_map<int, int> dict;
  inline int topXSum(const dict &cnt, int x) {
    int res = 0;

    vector<std::pair<int, int>> tmp(cnt.begin(), cnt.end());
    std::sort(tmp.begin(), tmp.end(), [](const auto &a, const auto &b) {
      if (a.second == b.second) {
        return a.first > b.first;
      }

      return a.second > b.second;
    });

    x = std::min(x, int(tmp.size()));

    for (int i = 0; i < x; i++) {
      res += tmp[i].first * tmp[i].second;
    }

    return res;
  }

public:
  vector<int> findXSum(vector<int> &nums, int k, int x) {
    const int n = nums.size();
    vector<int> res;
    dict cnt;

    for (int i = 0; i < k; i++) {
      cnt[nums[i]]++;
    }

    res.push_back(topXSum(cnt, x));

    for (int i = k; i < n; i++) {
      cnt[nums[i - k]]--;
      cnt[nums[i]]++;
      res.push_back(topXSum(cnt, x));
    }

    return res;
  }
};