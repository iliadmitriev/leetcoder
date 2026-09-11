#include <array>
#include <vector>

using std::array, std::vector;

class Solution {
public:
    int totalNumbers(vector<int>& digits) {
        int total = 0;

        array<int, 10> cnt = {0};
        for (int n : digits) {
            cnt[n]++;
        }

        for (int c = 1; c < 10; c++) {
            if (!cnt[c]) {
                continue;
            }

            cnt[c]--;

            for (int d = 0; d < 10; d++) {
                if (!cnt[d]) {
                    continue;
                }

                cnt[d]--;

                for (int u = 0; u < 10; u += 2) {
                    if (!cnt[u]) {
                        continue;
                    }

                    total++;
                }

                cnt[d]++;
            }

            cnt[c]++;
        }

        return total;
    }
};