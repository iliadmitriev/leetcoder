#include <algorithm>
#include <numeric>
#include <vector>
using std::vector;

class Solution {
public:
  double trimMean(vector<int> &arr) {
    std::sort(arr.begin(), arr.end());
    int n = arr.size();
    int k = n * 5 / 100;

    return std::accumulate(arr.begin() + k, arr.end() - k, 0.0) / (n - 2 * k);
  }
};