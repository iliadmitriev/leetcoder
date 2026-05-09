#include <numeric>
#include <unordered_map>
#include <vector>

using std::vector, std::unordered_map;
class Solution {
public:
  long long countBadPairs(vector<int> &nums) {
    const int N = nums.size();
    unordered_map<int, int> mp;

    for (int i = 0; i < N; ++i) {
      mp[nums[i] - i]++;
    }

    return std::accumulate(mp.begin(), mp.end(), 0LL,
                           [&](long long cnt, const auto &p) {
                             return cnt + (N - p.second) * p.second;
                           }) /
           2;
  }
};