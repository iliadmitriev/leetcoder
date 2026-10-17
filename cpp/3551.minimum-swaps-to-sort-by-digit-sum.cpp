#include <algorithm>
#include <tuple>
#include <vector>

using std::tuple, std::vector;

class Solution {
public:
    int minSwaps(vector<int>& nums) {
        auto sum_digits = [](int x) -> int {
            int y = 0;
            while (x > 0) {
                y += x % 10;
                x /= 10;
            }
            return y;
        };

        const int n = nums.size();
        vector<bool> vis(n, false); // S: O(n)
        vector<std::tuple<int, int, int>> arr; // S: O(n)
        arr.reserve(n);

        for (int i = 0; i < n; i++) {
            arr.emplace_back(sum_digits(nums[i]), nums[i], i);
        }

        std::ranges::sort(arr); // T: O(n log n)
        int swaps = 0;

        for (int i = 0; i < n; i++) {
          // if we already fixed order, or it's on its place -> skip
          if (vis[i] || std::get<2>(arr[i]) == i) {
            continue;
          }

          int j = i; // pointer to node
          int cycle = 0; // number of swaps for current cycle

          while (!vis[j]) {
            vis[j] = true;
            j = std::get<2>(arr[j]);
            cycle++;
          }

          swaps += cycle - 1;
        }

        return swaps;
    }
};