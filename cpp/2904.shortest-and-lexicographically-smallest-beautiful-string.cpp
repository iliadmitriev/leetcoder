class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        const int n = s.size();
        const char* v = s.data();

        int i = 0, j = 0, cur = 0;
        int best = n + 1;

        for (int l = 0, r = 0; r < n; r++) {
            cur += s[r] == '1';

            while ((l < r && s[l] == '0') || cur > k) {
                cur -= s[l++] == '1';
            }

            if (cur != k) {
                continue;
            }

            cout << "k: " << "l=" << l << " r=" << r << endl;

            if (r - l + 1 < best) {
                i = l;
                j = r + 1;
                best = r - l + 1;
            } else if (r - l + 1 == best &&
                       std::strncmp(v + l, v + i, best) < 0) {
                i = l;
                j = r + 1;
                best = r - l + 1;
            }
        }

        return s.substr(i, j - i);
    }
};