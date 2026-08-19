#include <unordered_map>
#include <vector>

using std::vector, std::unordered_map;

class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {
        unordered_map<int, uint8_t> rows;
        for (const auto& reservation : reservedSeats) {
            // collect all the seats reservation in groups of rows
            // also shift right (drop unused bits)
            const int i = reservation[0], j = reservation[1] - 2;
            if (j < 0 || j > 7) {
                continue;
            }

            rows[i] |= 1 << j;
        }

        const uint8_t m1 = 0b11110000;  // mask 1
        const uint8_t m2 = 0b00001111;  // mask 2
        const uint8_t m3 = 0b00111100;  // mask 3

        // count all the empty rows optimally,
        // 2 quad persons can fit in the empty row
        int total = (n - rows.size()) * 2;

        for (auto [_, occ] : rows) {
            if ((occ & m1) == 0 || (occ & m2) == 0 || (occ & m3) == 0) {
                total++;
            }
        }

        return total;
    }
};