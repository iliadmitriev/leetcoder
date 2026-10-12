#include <array>
#include <vector>

using std::vector, std::array;

class Solution {
public:
    int maxSum(vector<int>& nums, int k) {
        static const int SIZE = 30;
        static const int MOD = int(1e9) + 7;

        long long res = 0;
        array<int, SIZE> bits;

        for (int num : nums) {
#pragma unroll
            for (int i = 0; i < SIZE && num; i++) {
                bits[i] += (num >> i) & 1;
            }
        }

        for (; k; k--) {

            long long v = 0;

#pragma unroll
            for (int i = SIZE - 1; i >= 0; i--) {
                if (bits[i]-- > 0) {
                    v |= 1 << i;
                }
            }

            res = (res + v * v) % MOD;
        }

        return res;
    }
};