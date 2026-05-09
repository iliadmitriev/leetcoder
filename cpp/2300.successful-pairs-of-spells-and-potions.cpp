#include <vector>
using std::vector;

class Solution {
public:
  vector<int> successfulPairs(vector<int> &spells, vector<int> &potions,
                              long long success) {
    const int n = spells.size(), m = potions.size();
    vector<int> res(n);

    std::sort(potions.begin(), potions.end());

    std::transform(spells.begin(), spells.end(), res.begin(), [m, success, &potions](const int& spell) -> int{
      long target = (success + spell - 1) / spell;
      int cnt = std::lower_bound(potions.begin(), potions.end(), target) -
                potions.begin();
      return m - cnt;
    });

    return res;
  }
};