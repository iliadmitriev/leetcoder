#include <unordered_map>
#include <vector>

using std::vector, std::unordered_map;

class Solution {
public:
  int findLucky(vector<int> &arr) {
    unordered_map<int, int> cnt;
    for (int x : arr) {
      cnt[x]++;
    }

    int res = -1;

    for (auto [k, v] : cnt) {
      if (k == v && k > res)
        res = k;
    }

    return res;
  }
};