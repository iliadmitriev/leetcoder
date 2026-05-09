#include <algorithm>
#include <string>
#include <vector>

using std::string;
using std::vector;
class Solution {
public:
  int longestCommonPrefix(vector<int> &arr1, vector<int> &arr2) {
    vector<string> str1, str2;

    std::transform(arr1.begin(), arr1.end(), std::back_inserter(str1),
                   [](int x) { return std::to_string(x); });
    std::transform(arr2.begin(), arr2.end(), std::back_inserter(str2),
                   [](int x) { return std::to_string(x); });

    std::sort(str1.begin(), str1.end());
    std::sort(str2.begin(), str2.end());

    int i = 0, j = 0;
    int maxPrefixLen = 0;

    while (i < str1.size() && j < str2.size()) {
      int curPrefixLen = commonPrefixLen(str1[i], str2[j]);
      maxPrefixLen = std::max(maxPrefixLen, curPrefixLen);

      if (str1[i] == str2[j]) {
        i++;
        j++;
      } else if (str1[i] < str2[j]) {
        i++;
      } else {
        j++;
      }
    }

    return maxPrefixLen;
  }

private:
  int commonPrefixLen(const string &s1, const string &s2) {
    int n = std::min(s1.size(), s2.size());

    int i = 0;

    while (i < n && s1[i] == s2[i]) {
      i++;
    }

    return i;
  }
};