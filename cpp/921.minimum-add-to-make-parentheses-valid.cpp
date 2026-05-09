#include <stack>
#include <string>

using std::stack, std::string;

class Solution {
public:
  int minAddToMakeValid(string s) {
    stack<char> st;
    int counter = 0;

    for (char ch : s) {
      if (ch == '(') {
        st.push(ch);
      } else if (st.size() && ch == ')') {
        st.pop();
      } else if (ch == ')') {
        counter++;
      }
    }

    return counter + st.size();
  }
};