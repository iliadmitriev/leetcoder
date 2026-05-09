#include <vector>
using std::vector;

class Solution {
public:
  int minOperations(vector<int> &nums) {
    const int n = nums.size();
    vector<int> st;
    st.push_back(0);
    st.reserve(n);
    int ops = 0;

    for (int num : nums) {
      while (st.back() > num) {
        st.pop_back();
      }

      if (st.back() == num) {
        continue;
      }

      ops++;
      st.push_back(num);
    }

    return ops;
  }
};