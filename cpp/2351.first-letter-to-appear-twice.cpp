class Solution {
public:
    char repeatedCharacter(string s) {
       const char base = 'a';
       uint set = 0;

       for (char c : s) {
        if ((1 << (c - base)) & set) {
          return c;
        }

        set |= 1 << (c - base);
       }

       return 0;
    }
};