#include <vector>
using std::vector;

class Solution {
public:
  int maxDistance(vector<int> &colors) {
    int n = colors.size();
    int left = 0, right = n - 1;

    while (left < n && colors[left] == colors[n - 1]) {
      left++;
    }
    while (right >= 0 && colors[right] == colors[0]) {
      right--;
    }

    return std::max(right, n - left - 1);
  }
};