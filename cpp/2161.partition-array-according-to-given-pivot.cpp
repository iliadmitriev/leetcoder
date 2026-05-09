#include <vector>
using std::vector;

class Solution {
public:
  vector<int> pivotArray(vector<int> &nums, int pivot) {
    const int n = nums.size();
    vector<int> p, q;
    p.reserve(n);

    for (int i = 0; i < n; i++) {
      if (nums[i] < pivot) {
        p.push_back(nums[i]);
      } else if (nums[i] > pivot) {
        q.push_back(nums[i]);
      }
    }

    int count = n - p.size() - q.size();
    for (int i = 0; i < count; i++) {
      p.push_back(pivot);
    }

    p.insert(p.end(), q.begin(), q.end());

    return p;
  }
};