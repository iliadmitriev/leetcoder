#include <utility>
#include <vector>
using std::vector;

class Solution {
public:
  int maximumSwap(int num) {
    vector<int> st;
    while (num) {
      st.push_back(num % 10);
      num /= 10;
    }

    vector<int> maxPos;
    int curMax = st[0], curIdx = 0;
    for (int i = 0; i < st.size(); i++) {
      if (curMax < st[i]) {
        curMax = st[i];
        curIdx = i;
      }

      maxPos.push_back(curIdx);
    }

    for (int i = st.size() - 1; i > 0; i--) {
      if (st[i] < st[maxPos[i]]) {
        std::swap(st[i], st[maxPos[i]]);
        break;
      }
    }

    while (st.size()) {
      num *= 10;
      num += st.back();
      st.pop_back();
    }

    return num;
  }
};