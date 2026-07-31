#include <vector>
#include <string>
#include <algorithm>

using std::string;

class Solution {
public:
    int minimumPushes(string word) {
       const int N = 26;
       int count = 0, step = 0, i = 0;

       std::vector<int> cnt(N, 0);
       for (char ch : word) {
        cnt[ch - 'a']++;
       }

       std::ranges::sort(cnt, std::greater{});

       for (int c : cnt) {
          if (i % 8 == 0) {
            step++;
          }

          count += step * c;

          i++;
       }


       return count;

    }
};