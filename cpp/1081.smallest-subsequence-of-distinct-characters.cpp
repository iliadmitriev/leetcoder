class Solution {
public:
    string smallestSubsequence(string s) {
        char st[26]; // stack of unique chars
        int top = -1; // stack pointer

        bool added[26];
        int last[26];

        std::fill(added, added + 26, false); // {false, false, ... }

        // save the rightmost position of each character (last position)
        for (int i = 0; i < s.size(); i++) {
            last[s[i] - 'a'] = i;
        }

        for (int i = 0; i < s.size(); i++) {
            char ch = s[i];

            // skip character if it's already added (duplicate)
            if (added[ch - 'a']) {
                continue;
            }

            // if the current character has been met for the first time
            // and it's lexicographically less than stack's top character
            // and stack's top char is not unique and exist some where in the
            // future characters, then it can be removed (remove it, replace it for future char)
            while (top != -1 && ch < st[top] && i < last[st[top] - 'a']) {
                // remove from result stack;
                added[st[top] - 'a'] = false;
                top--; // pop
            }

            st[++top] = ch; // push
            added[ch - 'a'] = true;
        }

        return string(st, top + 1);
    }
};
