#include <vector>
using std::vector;

class Solution {
public:
  int maxArea(vector<int> &height) {
    int area = 0;

    for (vector<int>::iterator left = height.begin(), right = height.end() - 1;
         left < right;) {
      area = std::max(area, std::min(*left, *right) * int(right - left));

      if (*left < *right) {
        left++;
      } else {
        right--;
      }
    }

    return area;
  }
};