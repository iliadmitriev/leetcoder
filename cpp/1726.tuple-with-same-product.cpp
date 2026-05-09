#include <unordered_map>
#include <vector>

using std::vector, std::unordered_map;
class Solution {
public:
  int tupleSameProduct(vector<int> &nums) {

    const int N = nums.size();
    unordered_map<int, int> mp;
    int res = 0;

    for (int i = 0; i < N; ++i) {
      for (int j = i + 1; j < N; ++j) {
        mp[nums[i] * nums[j]]++;
      }
    }

    for (auto [_, v] : mp) {
      res += v * (v - 1);
    }

    return res * 4;
  }
};