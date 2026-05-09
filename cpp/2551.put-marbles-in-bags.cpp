#include <numeric>
#include <vector>

using std::vector;

/*
    cases:
    1. k = 0: return 0
    2. k = 1: return max(i, (weights[0] + weights[i]) + (weights[i+1] +
            weights[n-1])) - min(i, (weights[0] + weights[i]) + (weights[i+1] +
   weights[n-1]))

        i = 0 to n - 1


    weights[0] - weights[0] + weights[n-1] - weights[n - 1] +
    max(weights[i] + weights[i+1]) - min(weights[j] + weights[j+1])

    3. k = 2:
        return max(weights[i] + weights[i+1] + weights[j] +
   weights[j+1]) - min(weights[i] + weights[i+1] + weights[j] + weights[j+1])

        i < j
        i, j = 0 to n - 1

        ....

    n. k = len(weights): return 0

*/
class Solution {
public:
  long long putMarbles(vector<int> &weights, int k) {
    const int n = weights.size();
    vector<long> weightPairs(n - 1);

    if (k == 1 || k == n) {
      return 0;
    }

    for (int i = 0; i < n - 1; i++) {
      weightPairs[i] = weights[i] + weights[i + 1];
    }
    std::sort(weightPairs.begin(), weightPairs.end());

    k = k - 1; // cut the first and last
    return std::accumulate(weightPairs.end() - k, weightPairs.end(), 0L) -
           std::accumulate(weightPairs.begin(), weightPairs.begin() + k, 0L);
  }
};