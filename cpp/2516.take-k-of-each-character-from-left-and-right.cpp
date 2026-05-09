#include <string>
#include <vector>
using std::vector, std::string;

class Solution {
public:
  int takeCharacters(string s, int k) {
    vector<int> cnt(3, 0);
    for (char ch : s) {
      cnt[ch - 'a']++;
    }

    vector<int> need(3, 0);
    for (int i = 0; i < 3; i++) {
      if (cnt[i] - k < 0)
        return -1;

      need[i] = cnt[i] - k;
    }

    const int n = s.size();
    int maxLen = 0;
    vector<int> window(3, 0);
    int j = 0;

    for (int i = 0; i < n; i++) {
      window[s[i] - 'a']++;

      while (window[0] > need[0] || window[1] > need[1] ||
             window[2] > need[2]) {
        window[s[j] - 'a']--;
        j++;
      }

      maxLen = std::max(maxLen, i - j + 1);
    }

    return n - maxLen;
  }
};