#include <vector>

using std::vector;

class Solution {
public:
    int minimumEffort(vector<vector<int>>& tasks) {
        // sort list of tasks[actual amount, minimal amount]
        std::sort(tasks.begin(), tasks.end(),
                  [](const vector<int>& a, const vector<int>& b) -> bool {
                      int diff = a[1] - a[0] - b[1] + b[0];

                      // if difference is equal then sort by actual amount
                      if (diff == 0) {
                        return a[0] > b[0];
                      }

                      // descending sort by difference minimal and actual amount
                      return diff > 0;
                  });

        int res = 0, cur = 0;

        for (vector<int>& task : tasks) {

            if (cur < task[1]) {
                int diff = task[1] - cur;
                res += diff;
                cur += diff;
            }

            cur -= task[0];
        }

        return res;
    }
};