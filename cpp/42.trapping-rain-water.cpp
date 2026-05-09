#include <stack>

using namespace std;

class Solution {
public:
  int trap(vector<int> &height) {
    int water = 0;
    std::stack<int> st;

    for (int i = 0; i < height.size(); i++) {
      while (!st.empty() && height[st.top()] < height[i]) {
        int btm = st.top();
        st.pop();

        if (st.empty())
          break;

        water += (i - st.top() - 1) *
                 (min(height[st.top()], height[i]) - height[btm]);
      }

      st.push(i);
    }

    return water;
  }
};
