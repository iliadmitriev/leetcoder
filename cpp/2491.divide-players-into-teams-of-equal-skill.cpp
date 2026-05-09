#include <numeric>
#include <unordered_map>
#include <vector>

using std::vector, std::accumulate;
using IntMap = std::unordered_map<int, long>;

class Solution {
public:
  long long dividePlayers(vector<int> &skill) {
    long total = accumulate(skill.begin(), skill.end(), 0);
    int pairs = skill.size() / 2;

    if (total % pairs) {
      return -1;
    }
    int target = total / pairs;

    IntMap skillSet;
    for (int sk : skill) {
      skillSet[sk]++;
    }

    if (target % 2 == 0 && skillSet[target / 2] % 2) {
      return -1;
    } else if (target % 2 == 0) {
      skillSet[target / 2] /= 2;
    }

    long chemistry = 0;
    for (auto [k, v] : skillSet) {
      if (skillSet[target - k] != v) {
        return -1;
      }

      chemistry += k * (target - k) * v;
      skillSet[k] = 0;
      skillSet[target - k] = 0;
    }

    return chemistry;
  }
};