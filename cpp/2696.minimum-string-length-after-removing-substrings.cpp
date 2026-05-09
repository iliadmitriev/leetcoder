#include <string>
#include <stack>

using std::string, std::stack;

class Solution {
public:
    int minLength(string s) {
        stack<char> st;

        for (char ch : s) {
            if (st.size() && ((st.top() == 'A' && ch == 'B') || (st.top() == 'C' && ch == 'D'))) {
                st.pop();
            } else {
                st.push(ch);
            }
        }

        return st.size();     
    }
};