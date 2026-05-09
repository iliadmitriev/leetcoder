class Solution {
public:
    string decodeAtIndex(string s, int k) {
        long long length = 0;

        for (char ch : s) {
            if ('1' <= ch && ch <= '9') {
                length *= ch - '0';
            } else {
                length++;
            }
        }

        for (int i = s.size() - 1; i >= 0; i--) {
            k %= length;

            if (k == 0 && 'a' <= s[i] && s[i] <= 'z') {
                return string(1, s[i]);
            } else if ('1' <= s[i] && s[i] <= '9') {
                length /= s[i] - '0';
            } else {
                length--;
            }
        }
        return string("");
    }
};