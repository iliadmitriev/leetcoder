#include <stack>
#include <vector>

using namespace std;

class Solution {
private:
  int largestRectangleArea(const vector<int> &heights) {
    int n = heights.size();
    stack<int> st;
    int maxRect = 0;

    for (int i = 0; i <= n; i++) {
      int h = (i == n ? 0 : heights[i]);
      while (!st.empty() && (i == n || h < heights[st.top()])) {
        int preHeight = heights[st.top()];
        st.pop();
        int width = st.empty() ? i : i - st.top() - 1;

        maxRect = max(maxRect, preHeight * width);
      }

      st.push(i);
    }

    return maxRect;
  }

public:
  int maximalRectangle(vector<vector<char>> &matrix) {
    int m = matrix.size(), n = matrix[0].size();
    int maxArea = 0;
    vector<int> heights(n, 0);

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (matrix[i][j] == '1')
          heights[j]++;
        else
          heights[j] = 0;
      }
      maxArea = max(maxArea, largestRectangleArea(heights));
    }

    return maxArea;
  }
};