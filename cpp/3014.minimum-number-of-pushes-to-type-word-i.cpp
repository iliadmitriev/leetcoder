#include <string>
#include <vector>
#include <algorithm>

using std::string;

class Solution {
public:
    int minimumPushes(string word) {
        const int N = 26;
        std::vector<int> cnt(N, 0);
        int count = 0, step = 0, i = 0;

        for (char ch : word) {
            cnt[ch - 'a']++;
        }

        std::ranges::sort(cnt, std::greater{});

        for (int c : cnt) {
          if (i % 8 == 0) {
            step++;
          }
          
          count += c * step;

          i++;
        }

        return count;
    }
};