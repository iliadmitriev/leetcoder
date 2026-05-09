#include <algorithm>
#include <vector>
using std::vector;

class Solution {
public:
  int triangleNumber(vector<int> &nums) {
    std::sort(nums.begin(), nums.end());
    const int n = nums.size();
    int count = 0;

    // observations (a, b, c is indexes):
    // 1) a < b < c and a + b > c: triangle
    // 2) if (c-2) + (c-1) <= c: no solutions
    // 3) if 0 + 1 > c: all possible solutions

    // for (int a = 0; a < n; a++) {
    //   for (int b = a + 1; b < n; b++) {
    //     // look for lowest c side index:
    //     // bin search for nums[a] + nums[b], starting from b + 1
    //     int c = std::lower_bound(nums.begin() + b + 1, nums.end(),
    //                              nums[a] + nums[b]) -
    //             nums.begin();
    //     count += c - b - 1;
    //   }
    // }

    for (int c = n - 1; c > 1; c--) {
      // optimize 1: 0 + 1 > c
      // if all sides less than c, will be a triangle
      // count all triplet combinations as triangle and finish
      // 5 5 5 5 9
      if (nums[0] + nums[1] > nums[c]) {
        // C(x, 3) = x! / ((x - 3)! * 3!)
        // C(x, 3) = x * (x - 1) * (x - 2) / 6
        // x = c + 1
        count += (c + 1) * c * (c - 1) / 6;
        break;
      }

      // optimize 2: (c-2) + (c-1) <= c
      // if all possible sides will not be a triangle
      // c side is very large, no possible triangle
      // look for smaller c
      // 2 2 3 5
      if (nums[c - 2] + nums[c - 1] <= nums[c]) {
        continue;
      }

      int a = 0, b = c - 1;

      while (a < b) {
        if (nums[a] + nums[b] > nums[c]) {
          // triangles: number of indices between a and b (b - a + 1)
          // minus one for b side index (b - a + 1 - 1) => (b - a)
          count += b - a;
          b--;
        } else {
          a++;
        }
      }
    }

    return count;
  }
};