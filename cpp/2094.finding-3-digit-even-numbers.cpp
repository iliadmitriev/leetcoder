#include <array>
#include <vector>
using std::array, std::vector;

class Solution {
public:
  vector<int> findEvenNumbers(vector<int> &digits) {
    vector<int> out;
    array<int, 10> cnt;

    for (int d : digits) {
      cnt[d]++;
    }

    for (int d1 = 1; d1 < 10; d1++) {
      if (!cnt[d1]) {
        continue;
      }

      cnt[d1]--;
      for (int d2 = 0; d2 < 10; d2++) {
        if (!cnt[d2]) {
          continue;
        }

        cnt[d2]--;
        for (int d3 = 0; d3 < 10; d3 += 2) {
          if (!cnt[d3]) {
            continue;
          }

          out.push_back(d1 * 100 + d2 * 10 + d3);
        }
        cnt[d2]++;
      }
      cnt[d1]++;
    }

    return out;
  }
};