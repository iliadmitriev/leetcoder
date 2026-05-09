#include <stack>
#include <string>
#include <utility>
using std::string, std::stack, std::swap;

class Solution {
public:
  int minSwaps(string s) {
    stack<char> st;
    int n = s.size();
    int i = 0, j = n - 1;
    int swaps = 0;

    while (i < j) {

      while (i < j) {
        if (s[i] == '[') {
          st.push(s[i]);
        } else {
          if (st.size() && st.top() == '[') {
            st.pop();
          } else {
            break;
          }
        }

        i++;
      }

      while (i < j && s[j] == ']') {
        j--;
      }

      if (i == j) {
        break;
      }

      swaps++;
      st.push(']');
      swap(s[i], s[j]);
    }

    return swaps;
  }
};