#include <algorithm>
#include <cstdlib>
#include <string>

using std::string, std::max, std::min, std::abs;

class Solution {
public:
  int maxDistance(string s, int k) {
    int lat = 0, lon = 0;
    int longest = 0;
    const int n = s.size();

    for (int i = 0; i < n; i++) {
      switch (s[i]) {
      case 'N':
        lat++;
        break;
      case 'S':
        lat--;
        break;
      case 'W':
        lon--;
        break;
      case 'E':
        lon++;
        break;
      }

      longest = max(longest, min(abs(lat) + abs(lon) + 2 * k, i + 1));
    }

    return longest;
  }
};