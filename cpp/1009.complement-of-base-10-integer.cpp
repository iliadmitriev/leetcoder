#include <bit>

class Solution {
public:
    int bitwiseComplement(int n) {
        int mask = (1L << (32 - std::countl_zero(uint32_t(std::max(1, n))))) - 1;
        return mask ^ n;
    }
};