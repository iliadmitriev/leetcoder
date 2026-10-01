#include <string>
#include <vector>

using std::string, std::vector;

class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;

        for (char ch : s) {
            switch (ch) {
            case '(':
            case '[':
            case '{':
                stack.push_back(ch);
                break;
            case ')':
                if (stack.empty() || stack.back() != '(')
                    return false;
                stack.pop_back();
                break;
            case ']':
                if (stack.empty() || stack.back() != '[')
                    return false;
                stack.pop_back();
                break;
            case '}':
                if (stack.empty() || stack.back() != '{')
                    return false;
                stack.pop_back();
                break;
            default:
                return false;
            }
        }

        return stack.empty();
    }
};