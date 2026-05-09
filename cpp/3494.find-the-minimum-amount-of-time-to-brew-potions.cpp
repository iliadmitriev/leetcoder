#include <vector>
using std::vector;

class Solution {
public:
  long long minTime(vector<int> &skill, vector<int> &mana) {
    const int n = skill.size(), m = mana.size();
    long long shift = 0, totalShift = 0;

    vector<long long> starts(n), ends(n);

    std::partial_sum(skill.begin(), skill.end() - 1, starts.begin() + 1);
    std::partial_sum(skill.begin(), skill.end(), ends.begin());

    for (int i = 1; i < m; i++) {
      int prev = mana[i - 1], curr = mana[i];

      shift = prev * ends.front();
      for (int j = 0; j < n; j++) {
        shift = std::max(shift, prev * ends[j] - curr * starts[j]);
      }

      totalShift += shift;
    }

    return totalShift + ends.back() * mana.back();
  }
};