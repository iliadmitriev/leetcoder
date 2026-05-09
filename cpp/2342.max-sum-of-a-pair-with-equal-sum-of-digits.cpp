#include <unordered_map>
#include <utility>
#include <vector>

using std::vector, std::max, std::swap, std::unordered_map;

class Solution {
public:
  int maximumSum(vector<int> &nums) {
    int maxPairSum = -1;
    unordered_map<int, vector<int>> cache;

    for (auto num : nums) {
      cache[sumOfDigits(num)].push_back(num);
    }

    for (const auto &[_, v] : cache) {
      maxPairSum = max(maxPairSum, sumTwoMax(v));
    }

    return maxPairSum;
  }

private:
  int sumOfDigits(int n) {
    int s = 0;
    while (n) {
      s += n % 10;
      n /= 10;
    }
    return s;
  }

  int sumTwoMax(const vector<int> &arr) {
    if (arr.size() < 2) {
      return -1;
    }

    int max1 = arr[0], max2 = arr[1];
    int N = arr.size();

    if (max1 < max2) {
      swap(max1, max2);
    }

    for (int i = 2; i < N; i++) {
      if (arr[i] > max1) {
        max2 = max1;
        max1 = arr[i];
      } else if (arr[i] > max2) {
        max2 = arr[i];
      }
    }

    return max1 + max2;
  }
};