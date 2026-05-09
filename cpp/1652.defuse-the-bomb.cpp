#include <vector>

using std::vector;

class Solution {
public:
  vector<int> decrypt(vector<int> &code, int k) {
    int n = code.size();
    vector<int> res(n, 0);

    if (k == 0) {
      return res;
    }

    /* for start pointing at 0
     * k > 0  left = 1, right = k + 1
     * k < 0  left = n + k, right = n
     */
    int left = (k > 0) ? 1 : n + k, right = (k > 0) ? k + 1 : n;
    int window = 0;

    for (int i = left; i < right; i++) {
      window += code[i];
    }

    for (int i = 0; i < n; i++) {
      res[i] = window;
      window += code[(i + right) % n] - code[(i + left) % n];
    }

    return res;
  }
};