#include <vector>
using std::vector;

class Solution {
public:
  vector<int> lexicalOrder(int n) {
    vector<int> result;
    result.reserve(n);

    int cur = 1;

    for (int i = 0; i < n; i++) {
      result.push_back(cur);

      if (cur * 10 <= n) {
        cur *= 10;
      } else {

        while (cur % 10 == 9 || cur >= n) {
          cur /= 10;
        }

        cur++;
      }
    }

    return result;
  }
};