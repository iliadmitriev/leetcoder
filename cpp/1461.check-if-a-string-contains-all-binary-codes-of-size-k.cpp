#include <vector>

using std::vector;

class Solution {
public:
    bool hasAllCodes(string s, int k) {
        const int n = s.size(), mask = (1 << k) - 1;

        int cur = 0;       // current value
        int rest = 1 << k; // how much distinct values left to collect, goal

        if (n - k + 1 < mask) {
            return false;
        }

        vector<bool> acc(mask); // distinct values accumulator

        for (int i = 0; i < n; i++) {
            // remove leftmost digit
            // add rihtmost digit
            cur = (cur << 1) & mask | s[i] == '1';

            // if current length of value is less than k
            if (i + 1 < k) {
                continue;
            }

            // check if value is distinct and add it to accumulator
            if (!acc[cur]) {
                rest--;
            }

            acc[cur] = true;

            // early return if goal is reached
            if (rest == 0) {
                return true;
            }

            // if there is not enough digits to accomplish rest of the goal
            if (n - i - 1 < rest) {
                return false;
            }
        }

        return rest == 0;
    }
};