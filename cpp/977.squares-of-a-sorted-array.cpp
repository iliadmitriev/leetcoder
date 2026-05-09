#include <vector>
using std::vector;

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
      const int n = nums.size();
      int i = 0, j = n - 1;
      int k = n - 1;

      vector<int> res(n, 0);

      while (i <= j) {
        int a = nums[i], b = nums[j];
        a *= a;
        b *= b;

        if (a > b) {
          res[k--] = a;
          i++;
        } else {
          res[k--] = b;
          j--;
        }
      }

      return res;
    }
};