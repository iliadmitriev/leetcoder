#include <string>
using std::string;

class Solution {
public:
    string removeOuterParentheses(string s) {
        string res;
        res.reserve(s.size());
        int d = 0;
        
        for (char ch : s) {
            if (ch == '(' && d > 0) {
                res.push_back(ch);
            } else if (ch == ')' && d > 1) {
                res.push_back(ch);
            }
            
            if (ch == '(') {
                d++; 
            } else {
                d--;
            }
        }
        
        return res;
        
    }
};