class Solution {
public:
    string removeDuplicateLetters(string s) {
        
        char st[26];
        int top = -1;
        bool added[26];
        int last[26];
        for (int i = 0; i < s.size(); i++) { last[s[i] - 'a'] = i; }
        for (int i = 0; i < 26; ++i) { added[i] = false; }

        for (int i = 0; i < s.size(); i++) {
            char ch = s[i];

            if (added[ch - 'a']) {
                continue;
            }

            while (top != -1 && ch < st[top] && i < last[st[top] - 'a']) {
                // remove from result stack;
                added[st[top] - 'a'] = false;
                top--;
            }

            st[++top] = ch;
            added[ch - 'a'] = true;
        }

        return string(st, top + 1);
    }
};