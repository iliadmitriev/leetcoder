#include <algorithm>
#include <queue>
#include <vector>

using std::vector, std::priority_queue;
class Solution {
public:
  int maxRemoval(vector<int> &nums, vector<vector<int>> &queries) {
    const int n = nums.size(), m = queries.size();
    vector<int> diff(n + 1, 0); // queries cummulative value
    priority_queue<int> pq;     // max heap for query right bounds
    int j = 0;                  // query index
    int cur = 0;                // current cumulative value

    // order queries by left bound
    std::sort(queries.begin(), queries.end());

    for (int i = 0; i < n; i++) {
      cur += diff[i];
      // add all queries right bounds with the same left bound to max heap
      while (j < m && queries[j][0] == i) {
        pq.push(queries[j][1]);
        j++;
      }

      // pop queries from heap until current num is smaller or equal to current
      // cummulative value
      while (cur < nums[i] and !pq.empty() and pq.top() >= i) {
        cur++;
        diff[pq.top() + 1]--;
        pq.pop();
      }

      if (cur < nums[i]) {
        return -1;
      }
    }

    return pq.size();
  }
};