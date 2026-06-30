class Solution {
public:
    int numberOfSubstrings(string s) {
        const int n = s.size();

        int cnt[] = {0, 0, 0};
        int win = 0, res = 0;
        int i = 0;

        for (int j = 0; j < n; j++) {
            cnt[s[j] - 'a']++;

            while (cnt[0] && cnt[1] && cnt[2]) {
                win++;
                cnt[s[i] - 'a']--;
                i += 1;
            }

            res += win;
        }

        return res;
    }
};