#include <algorithm>
#include <vector>
using std::vector;

class Solution {
public:
  int numberOfEmployeesWhoMetTarget(vector<int> &hours, int target) {
    return std::count_if(hours.begin(), hours.end(),
                         [target](int h) { return h >= target; });
  }
};