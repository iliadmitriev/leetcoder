#include <vector>
using std::vector;

class Solution {
public:
    int sortableIntegers(vector<int>& nums) {
        const int n = nums.size();
        int res = 0;

        // factorize n into div
        vector<int> div;
        for (int d = 1; d * d <= n; d++) {
            if (n % d == 0) {
                div.push_back(d);

                if (n / d != d) {
                    div.push_back(n / d);
                }
            }
        }

        // nextDescent[i] - index of the next descending element from i onward
        // to n
        vector<int> nextDescent(n, n);
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] > nums[i + 1]) {
                nextDescent[i] = i;
            } else {
                nextDescent[i] = nextDescent[i + 1];
            }
        }

        // check if array nums can be done sorted with window == k
        auto isSortedWin = [&nums, &nextDescent, &n](int k) -> bool {
            int prev = 0;

            for (int r = k - 1; r < n; r += k) {
                int l = r - k + 1;
                int drop = nextDescent[l];

                // if drop is not withing window bounds
                // case 1: the window is sorted
                if (drop > r) {
                    // connects to previos window
                    if (prev > nums[l]) {
                        return false;
                    }

                    prev = nums[r];

                } else {
                    // case 2: window has at least one drop inside its bounds
                    // it's fixable if:
                    // * this drop is only one (no other drop)
                    // * joined window parts after rotation is sorted
                    // * connects to previos window
                    if (nextDescent[drop + 1] < r || nums[r] > nums[l] ||
                        prev > nums[drop + 1]) {
                        return false;
                    }

                    prev = nums[drop];
                }
            }
            return true;
        };

        for (int d : div) {
            if (isSortedWin(d)) {
                res += d;
            }
        }

        return res;
    }
};