#include <string>

using namespace std;

class Solution {
public:
  string makeGood(std::string s) {
    string st;
    st.reserve(s.size());

    for (char c : s) {
      if (!st.empty() && abs(c - st.back()) == 32) {
        st.pop_back();
      } else {
        st.push_back(c);
      }
    }

    return st;
  }
};