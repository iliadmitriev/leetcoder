class Solution {
public:
    string reverseWords(string s) {

        auto start = s.begin();
        auto end = s.begin();

        while (start != s.end()) {
            while (end != s.end() && *end != ' ') {
                end++;
            }
            std::reverse(start, end);
            if (end != s.end()) end++;
            start = end;
        }

        return s;
    }
};