#include <string>
using std::string;

class Solution {
private:
  const static int SIZE = 26;
  bool match(const int *a, const int *b) {
    for (int i = 0; i < SIZE; ++i)
      if (a[i] != b[i])
        return false;
    return true;
  }

public:
  bool checkInclusion(string s1, string s2) {
    int m = s1.size(), n = s2.size();
    if (m > n) {
      return false;
    }

    int pattern[SIZE] = {0};
    int window[SIZE] = {0};

    for (int i = 0; i < m; ++i) {
      pattern[s1[i] - 'a']++;
      window[s2[i] - 'a']++;
    }

    int count = 0;
    for (int i = 0; i < SIZE; ++i) {
      if (pattern[i] == window[i]) {
        ++count;
      }
    }

    if (count == SIZE) {
      return true;
    }

    for (int i = m; i < n; ++i) {
      int left = s2[i - m] - 'a';
      int right = s2[i] - 'a';

      window[left]--;
      count += window[left] == pattern[left]       ? 1
               : window[left] + 1 == pattern[left] ? -1
                                                   : 0;

      window[right]++;
      count += window[right] == pattern[right]       ? 1
               : window[right] - 1 == pattern[right] ? -1
                                                     : 0;

      if (count == SIZE) {
        return true;
      }
    }

    return false;
  }
};