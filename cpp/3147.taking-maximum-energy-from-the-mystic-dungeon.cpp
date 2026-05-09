#include <vector>
using std::vector;

class Solution {
public:
  int maximumEnergy(vector<int> &energy, int k) {
    const int n = energy.size();

    vector<int> prefix(n, 0);

    for (int i = 0; i < n; i++) {
      prefix[i] = energy[i];

      if (i >= k) {
        prefix[i] = std::max(prefix[i], prefix[i] + prefix[i - k]);
      }
    }

    return *std::max_element(prefix.end() - k, prefix.end());
  }
};