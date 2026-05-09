class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.size();

        while (l < r) {

            while (l < r && !std::isalnum(s[l])) {
                l++;
            }
            while (l < r && !std::isalnum(s[r])) {
                r--;
            }

            if (tolower(s[l]) != tolower(s[r])) {
                return false;
            }

            l++; r--;
        }

        return true;
    }
};