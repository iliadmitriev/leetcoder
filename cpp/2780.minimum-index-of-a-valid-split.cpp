#include <algorithm>
#include <vector>
using std::vector;

class Solution {
private:
  int getDominant(const vector<int> &arr) {
    int res = -1, cnt = 0;
    for (int v : arr) {
      if (cnt == 0) {
        res = v;
      }
      cnt += res == v ? 1 : -1;
    }

    return res;
  }

public:
  int minimumIndex(vector<int> &nums) {
    const int dom = getDominant(nums), n = nums.size();
    int left = 0, right = std::count(nums.begin(), nums.end(), dom);

    if (right * 2 < n) {
      return -1;
    }

    for (int i = 0; i < n; i++) {
      if (nums[i] == dom) {
        left++;
        right--;
      }

      if ((left * 2 > i + 1) && (right * 2 > (n - i - 1))) {
        return i;
      }
    }

    return -1;
  }
};