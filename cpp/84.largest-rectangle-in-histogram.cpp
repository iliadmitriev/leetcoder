#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
  int largestRectangleArea(vector<int> &heights) {
    stack<pair<int, int>> st;
    int maxArea = 0;
    int n = heights.size();

    for (int i = 0; i <= n; i++) {
      int height = (i == n) ? 0 : heights[i];
      int start = i;

      while (!st.empty() && st.top().second > height) {
        auto [prevStart, prevHeight] = st.top();
        st.pop();
        maxArea = max(maxArea, prevHeight * (i - prevStart));
        start = prevStart;
      }

      st.push({start, height});
    }

    return maxArea;
  }
};