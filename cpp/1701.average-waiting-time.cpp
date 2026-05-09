#include <vector>

using std::vector;

class Solution {
public:
  double averageWaitingTime(vector<vector<int>> &customers) {
    long total = 0, start = 0, idleAt = 0;

    for (const auto &c : customers) {
      start = idleAt > c[0] ? idleAt : c[0];
      total += start - c[0];
      total += c[1];
      idleAt = start + c[1];
    }

    return (double)total / customers.size();
  }
};