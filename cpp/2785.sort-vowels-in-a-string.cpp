class Solution {
private:
    bool isVow(char ch) {
        return ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U' || ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
    }
public:
    string sortVowels(string s) {
        vector<int> w('u' - 'A' + 1, 0);
        for (char ch : s) {
            if (isVow(ch)) {
                w[ch - 'A']++;
            }
        }

        int j = 0;
        for (int i = 0; i < s.size(); i++) {
            if (!isVow(s[i])) {
                continue;
            }

            while (w[j] == 0) {
                j++;
            }

            s[i] = 'A' + j;
            w[j]--;
        }

        return s;
    }
};