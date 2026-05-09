#include <bit>

class Solution {
public:
    vector<int> sortByBits(vector<int>& arr) {
        sort(arr.begin(), arr.end(), [](int a, int b) -> bool {
            // <--- bits count --> <------ bits ----->
            // 0000 0000 0000 0110 0000 0000 1101 1011
            int v1 = std::popcount(uint(a)) << 16 | a;
            int v2 = std::popcount(uint(b)) << 16 | b;

            return v1 < v2;
        });

        return arr;
    }
};