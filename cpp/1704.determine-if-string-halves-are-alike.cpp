class Solution {
public:
    bool halvesAreAlike(string s) {
        int n = s.size();
        int mid = n / 2;
        set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        int count = 0;

        for (int i = 0; i < n; i++) {
            if (vowels.find(s[i]) == vowels.end()) {
                continue;
            }

            if (i < mid) {
                count++;
            } else {
                count--;
            }
        }

        return count == 0;
    }
};