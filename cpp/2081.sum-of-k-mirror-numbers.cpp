#include <vector>
using std::vector;

class Solution {
private:
  // mirror the number
  long long mirror(int num, bool odd) {
    long long res = num, x = odd ? num : num / 10;

    while (x) {
      res = res * 10 + x % 10;
      x /= 10;
    }

    return res;
  }

  // check number is a palindrome
  bool isPalindrome(long long num, int k) {
    vector<int> tmp;
    while (num) {
      tmp.push_back(num % k);
      num /= k;
    }

    for (int i = 0, j = tmp.size() - 1; i < j; i++, j--) {
      if (tmp[i] != tmp[j]) {
        return false;
      }
    }

    return true;
  }

public:
  long long kMirror(int k, int n) {
    int count = 0;
    long long total = 0L;

    int next, prev = 1;

    while (count < n) {
      next = 10 * prev;

      for (bool odd : {false, true}) {
        for (int x = prev; x < next; x++) {
          if (count == n) {
            return total;
          }

          long long value = mirror(x, odd);

          if (isPalindrome(value, k)) {
            total += value;
            count++;
          }
        }
      }

      prev = next;
    }

    return total;
  }
};