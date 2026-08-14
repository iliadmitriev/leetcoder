#include <string>
#include <vector>

using std::vector, std::string;

class Solution {
public:
    int maximumLengthSubstring(string s) {
        vector<int> win(26);
        const int n = s.size();
        int largest = 0;

        for (int i = 0, j = 0; i < n; i++) {
            win[s[i] - 'a']++;

            while (win[s[i] - 'a'] > 2) {
                win[s[j++] - 'a']--;
            }

            largest = std::max(largest, i - j + 1);
        }

        return largest;
    }
};