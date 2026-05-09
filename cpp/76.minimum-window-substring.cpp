class Solution {
public:
    string minWindow(string s, string t) {
        int m = s.size(); int n = t.size();
        vector<int> need(60, 0); // lower and upper case english
        vector<int> window(60, 0); // lower and upper case english

        for (char ch: t) { need[ch - 'A']++; }

        int l = 0;
        int completed = 0;
        pair<int,int> res = {0, 0}; // left pointer, length;

        for (int r = 0; r < m; r++) {
            if (need[s[r] - 'A'] > 0) {
                window[s[r] - 'A']++;

                if (need[s[r] - 'A'] >= window[s[r] - 'A']) {
                    completed++;
                }
            }

            while (completed == n && l <= r) {

                if (!res.second || res.second > r + 1 - l) {
                    res = {l, r + 1 - l};
                }

                if (window[s[l] - 'A'] > 0) {
                    window[s[l] - 'A']--;

                    if (need[s[l] - 'A'] > window[s[l] - 'A']) {
                        completed--;
                    }
                }

                l++;
            }
        }

        return s.substr(res.first, res.second);
    }
};