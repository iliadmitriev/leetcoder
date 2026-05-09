class Solution {
private:
    bool isVowel(char ch) {
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
            return 1;
        }
        return 0;
    }

public:
    int maxVowels(string s, int k) {
        int maxVow = 0, curVow = 0;
        int n = s.size();
        for (int i = 0; i < k; i++) {
            curVow += isVowel(s[i]);
        }

        maxVow = max(maxVow, curVow);

        for (int i = k; i < n; i++) {
            curVow -= isVowel(s[i - k]);
            curVow += isVowel(s[i]);
            maxVow = max(maxVow, curVow);
        }

        return maxVow;
    }
};