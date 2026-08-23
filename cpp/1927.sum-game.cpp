#include <string>
#include <utility>

using std::string, std::pair;

class Solution {
public:
    bool sumGame(string num) {
        auto collect = [&num](int l, int r) -> pair<int, int> {
            int n = 0, q = 0;
            for (; l < r; l++) {
                if (num[l] == '?') {
                    q++;
                } else {
                    n += num[l] - '0';
                }
            }

            return {n, q};
        };

        int n = num.size();
        auto [n0, q0] = collect(0, n / 2);
        auto [n1, q1] = collect(n / 2, n);

        return (q0 + q1) % 2 == 1 || n0 - n1 != (q1 - q0) * 9 / 2;
    }
};