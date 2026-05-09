class Solution {
private:
    bool isPalindrome(const string& s, int i, int j) {
        if (i < 0 || j > s.size() - 1 || j < i) {
            return false;
        }
        while (i < j) {
            if (s[i] != s[j]) {
                return false;
            }
            i++; j--;
        }
        return true;
    }

public:
    string longestPalindrome(string s) {
        int left = 0;
        int length = 1;

        for (int right = 1; right < s.size(); right++) {
            int left_even = right - length;
            int left_odd = right - length - 1;

            if (right + 1 - left_even > length && isPalindrome(s, left_even, right)) {
                left = left_even;
                length = right + 1 - left_even;
            }

            if (right + 1 - left_odd > length && isPalindrome(s, left_odd, right)) {
                left = left_odd;
                length = right + 1 - left_odd;
            }

        }

        return s.substr(left, length);
    }
};