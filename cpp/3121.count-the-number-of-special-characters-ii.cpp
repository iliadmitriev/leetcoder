#include <array>
#include <cctype>
#include <string>

class Solution {
public:
    int numberOfSpecialChars(string word) {
        const int n = word.size();

        std::array<int, 26> lower = {}, upper = {};
        int count = 0;

        for (int i = 0; i < n; i++) {
            const char ch = word[i];

            if (std::islower(ch)) {
                lower[ch - 'a'] = i + 1;
            } else if (!upper[ch - 'A']) {
                upper[ch - 'A'] = i + 1;
            }
        }

        for (int i = 0; i < 26; i++) {
            if (lower[i] > 0 && lower[i] < upper[i]) {
                count++;
            }
        }

        return count;
    }
};