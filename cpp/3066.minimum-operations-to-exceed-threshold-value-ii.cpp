#include <functional>
#include <queue>
#include <vector>

using std::vector, std::priority_queue, std::greater;

class Solution {
public:
  int minOperations(vector<int> &nums, int k) {
    priority_queue<long, vector<long>, greater<long>> pq(nums.begin(),
                                                         nums.end());
    int ops = 0;

    while (pq.size() > 1 && pq.top() < k) {
      ops++;

      long v = 0;

      v += pq.top() * 2;
      pq.pop();
      v += pq.top();
      pq.pop();

      pq.push(v);
    }

    return ops;
  }
};