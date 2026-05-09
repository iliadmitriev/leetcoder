#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
private:
  // build full palindrome from it's left part
  long buildPalindrome(long left, bool odd) {
    long res = left;

    if (odd)
      left /= 10;

    while (left) {
      res *= 10;
      res += left % 10;
      left /= 10;
    }

    return res;
  }

public:
  string nearestPalindromic(string n) {
    int size = n.size();

    int mid =
        size % 2 ? size / 2 : size / 2 - 1; // mid shifted left for odd size

    long left = std::stol(n.substr(0, mid + 1)); // left part of input string

    vector<long> candidates = {
        buildPalindrome(left, size % 2),     // 12355321
        buildPalindrome(left - 1, size % 2), // 12344321
        buildPalindrome(left + 1, size % 2), // 12366321
        (long)std::pow(10, size - 1) - 1,    // 9999999999
        (long)std::pow(10, size) + 1,        // 1000000001
    };

    long diff = LONG_MAX;
    long res = 0;
    long int_n = std::stol(n);

    for (auto cand : candidates) {
      if (cand == int_n)
        continue;

      if (abs(cand - int_n) < diff) {
        diff = abs(cand - int_n);
        res = cand;
      } else if (abs(cand - int_n) == diff) {
        res = std::min(res, cand);
      }
    }

    return std::to_string(res);
  }
};