#include <array>
#include <string>

using std::string, std::array;

class Solution {
public:
  int numberOfSubstrings(string s) {
    array<int, 3> win;
    const int n = s.size();
    int count = 0, left = 0;

    for (int right = 0; right < n; right++) {
      win[s[right] - 'a']++;
      while (win[0] && win[1] && win[2]) {
        count += n - right;
        win[s[left++] - 'a']--;
      }
    }

    return count;
  }
};