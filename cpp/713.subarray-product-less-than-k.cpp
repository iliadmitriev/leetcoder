class Solution {
public:
  int numSubarrayProductLessThanK(vector<int> &nums, int k) {
    int prod = 1;
    int p = 0;
    int res = 0;

    for (int q = 0; q < nums.size(); q++) {
      prod *= nums[q];

      while (p <= q && prod >= k) {
        prod /= nums[p];
        p++;
      }

      res += (q - p + 1);
    }

    return res;
  }
};