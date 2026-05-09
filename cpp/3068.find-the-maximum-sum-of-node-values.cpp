long long min(long long a, long long b) { return a < b ? a : b; }

class Solution {
public:
  long long maximumValueSum(vector<int> &nums, int k,
                            vector<vector<int>> &edges) {
    // XOR can be applied to any pair of nodes, even without an edge connecting
    // them. since there is a path between these two nodes and there is no
    // cycles.
    long long base = 0;
    long long totalIncreaseDelta = 0;
    long long numIncrease = 0, numDecrease = 0;
    long long minIncrease = numeric_limits<long long>::max();
    long long minDecrease = numeric_limits<long long>::max();

    for (auto num : nums) {
      base += num;
      if ((num ^ k) > num) {
        numIncrease++;
        totalIncreaseDelta += (num ^ k) - num;
        minIncrease = min(minIncrease, (num ^ k) - num);
      } else {
        numDecrease++;
        minDecrease = min(minDecrease, num - (num ^ k));
      }
    }

    if (!numIncrease) {
      return base;
    }

    if (numIncrease % 2 == 0) {
      return base + totalIncreaseDelta;
    }

    if (numDecrease == 0) {
      return base + totalIncreaseDelta - minIncrease;
    }

    return base + totalIncreaseDelta - min(minIncrease, minDecrease);
  }
};