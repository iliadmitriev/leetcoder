#include <numeric>
#include <vector>

using std::vector;

class Solution {
public:
  vector<int> lexicographicallySmallestArray(vector<int> &nums, int limit) {
    const int N = nums.size();
    vector<int> res(N);
    int groupIdx = 0;
    vector<int> posToGroup(N, -1);
    vector<int> groupStart = {0};

    vector<int> sortedNums(N);
    std::iota(sortedNums.begin(), sortedNums.end(), 0);
    std::sort(sortedNums.begin(), sortedNums.end(),
              [&nums](int i1, int i2) -> bool { return nums[i1] < nums[i2]; });

    int prev = nums[sortedNums.front()];

    for (int j = 0; j < N; ++j) {
      int i = sortedNums[j];
      int num = nums[i];

      if (num - prev > limit) {
        groupIdx++;
        groupStart.push_back(j);
      }

      posToGroup[i] = groupIdx;
      prev = num;
    }

    for (int j = 0; j < N; ++j) {
      int group = posToGroup[j];

      res[j] = nums[sortedNums[groupStart[group]]];
      groupStart[group]++;
    }

    return res;
  }
};