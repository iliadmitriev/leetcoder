#include <numeric>
#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
  vector<int> survivedRobotsHealths(vector<int> &positions,
                                    vector<int> &healths, string directions) {
    int n = positions.size();
    vector<int> idx(n);
    std::iota(idx.begin(), idx.end(), 0);
    std::sort(idx.begin(), idx.end(), [&positions](int i, int j) {
      return positions[i] < positions[j];
    });

    vector<int> st;

    for (int pos : idx) {
      while (st.size() && directions[st.back()] == 'R' &&
             directions[pos] == 'L' && healths[pos] > 0) {
        int top = st.back();
        st.pop_back();

        if (healths[top] > healths[pos]) {
          healths[top]--;
          healths[pos] = 0;
          pos = top;
          n--;
          break;
        } else if (healths[top] < healths[pos]) {
          healths[pos]--;
          healths[top] = 0;
          n--;
        } else {
          healths[pos] = healths[top] = 0;
          n -= 2;
        }
      }

      if (healths[pos] > 0) {
        st.push_back(pos);
      }
    }

    vector<int> res;
    res.reserve(n);
    for (int h : healths) {
      if (h > 0)
        res.push_back(h);
    }

    return res;
  }
};