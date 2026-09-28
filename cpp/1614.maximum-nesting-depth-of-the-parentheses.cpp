#include <string>

using std::string;

class Solution {
public:
    int maxDepth(string s) {
        int maxDepth = 0, depth = 0;

        for (char ch : s) {
            switch (ch) {
            case '(':
                depth++;
                break;
            case ')':
                depth--;
                break;
            default:
            }

            maxDepth = std::max(maxDepth, depth);
        }

        return maxDepth;
    }
};