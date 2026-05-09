#include <ios>
#include <iostream>
#include <string>
using std::string;

const int ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);

  return 0;
}();

class Solution {
public:
  bool canMakeSubsequence(string str1, string str2) {
    const int m = str1.size(), n = str2.size();
    if (m < n) {
      return false;
    }

    int i = 0, j = 0;
    while (i < m && j < n && m - i >= n - j) {
      if (str2[j] == str1[i] || str2[j] == (str1[i] - 96) % 26 + 97) {
        j++;
      }

      i++;
    }

    if (j == n) {
      return true;
    }

    return false;
  }
};