#include <vector>
using std::vector;

class Solution {
private:
  int bisectLeft(const vector<int> &arr, int x) {
    int lo = 0, hi = arr.size();
    int mid;

    while (lo < hi) {
      mid = (lo + hi) / 2;

      if (arr[mid] < x) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }

    return lo;
  }

  int bisectRight(const vector<int> &arr, int x) {
    int lo = 0, hi = arr.size();
    int mid;

    while (lo < hi) {
      mid = (lo + hi) / 2;

      if (arr[mid] > x) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }

    return lo;
  }

  int maxTotalFruitsV1(vector<vector<int>> &fruits, int startPos, int k) {
    const int n = fruits.size();
    vector<int> pos(n, 0);
    vector<int> prefix(n + 1, 0);

    for (int i = 0; i < n; i++) {
      pos[i] = fruits[i][0];
      prefix[i + 1] = prefix[i] + fruits[i][1];
    }

    int curMax = 0, left, right, start, end;
    for (int x = 0; x <= k / 2; x++) {
      left = startPos - x;
      right = startPos + k - 2 * x;

      start = bisectLeft(pos, left);
      end = bisectRight(pos, right);

      curMax = std::max(curMax, prefix[end] - prefix[start]);

      left = startPos - k + 2 * x;
      right = startPos + x;

      start = bisectLeft(pos, left);
      end = bisectRight(pos, right);

      curMax = std::max(curMax, prefix[end] - prefix[start]);
    }

    return curMax;
  }

  int stepsCount(const vector<vector<int>> &fruits, int startPos, int left,
                 int right) {
    int leftPart = startPos - fruits[left][0];
    int rightPart = fruits[right][0] - startPos;
    int bothParts = rightPart + leftPart;

    if (startPos <= fruits[left][0]) {
      return rightPart;
    } else if (startPos >= fruits[right][0]) {
      return leftPart;
    }

    return std::min(leftPart, rightPart) + bothParts;
  }

  int maxTotalFruitsV2(vector<vector<int>> &fruits, int startPos, int k) {
    const int n = fruits.size();
    int cur = 0, curMax = 0, left = 0;

    for (int right = 0; right < n; right++) {
      cur += fruits[right][1];

      while (left <= right && stepsCount(fruits, startPos, left, right) > k) {
        cur -= fruits[left][1];
        left++;
      }

      curMax = std::max(curMax, cur);
    }
    return curMax;
  }

public:
  int maxTotalFruits(vector<vector<int>> &fruits, int startPos, int k) {
    return maxTotalFruitsV2(fruits, startPos, k);
  }
};