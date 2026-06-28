#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        std::ranges::sort(arr);

        int prev = 0;
        for (int num : arr) {
            prev = std::min(prev + 1, num);
        }

        return prev;
    }
};