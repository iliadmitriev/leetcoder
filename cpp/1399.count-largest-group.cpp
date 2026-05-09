#include <vector>

using std::vector;

class Solution {
public:
  int countLargestGroup(int n) {
    int limit = sumDigit(10000 - 1) + 1;
    vector<int> counter(limit, 0);

    for (int i = 1; i <= n; i++) {
      int key = sumDigit(i);
      counter[key]++;
    }

    int largest = 0, largestCount = 0;
    for (int cnt : counter) {
      if (largest < cnt) {
        largest = cnt;
        largestCount = 1;
      } else if (largest == cnt) {
        largestCount++;
      }
    }

    return largestCount;
  }

private:
  int sumDigit(int n) {
    int result = 0;
    while (n) {
      result += n % 10;
      n /= 10;
    }

    return result;
  }
};