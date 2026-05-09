#include <deque>
#include <vector>

using std::deque;
using std::vector;

class Solution {
public:
  int numberOfSubarrays(vector<int> &nums, int k) {
    deque<int> q;
    int count = 0;
    int prev = -1;

    for (int i = 0; i < nums.size(); i++) {
      if (nums[i] % 2) {
        q.push_back(i);
      }

      if (q.size() > k) {
        prev = q.front();
        q.pop_front();
      }

      if (q.size() == k) {
        count += q.front() - prev;
      }
    }

    return count;
  }
};