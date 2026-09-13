#include <vector>
#include <unordered_map>
#include <ranges>

using std::vector, std::unordered_map;

class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        const int n = img1.size();
        vector<pair<int, int>> ones1, ones2;

        for (int i = 0; i < n; i++) {
          for (int j = 0; j < n; j++) {
              if (img1[i][j]) {
                ones1.push_back({i, j});
              }

              if (img2[i][j]) {
                ones2.push_back({i, j});
              }
          }
        }

        // key shift (n = 30): 
        // min: 30 + 0 - 30 = 0
        // max: 30 + 30 - 0 = 60
        // to store values in range [0; 60] we need 6 bit (shift=6, max_value=64)
        // key: drow << 6 | dcol
        const int shift = 6;
        unordered_map<int, int> freq;

        for (auto [r1, c1] : ones1) {
          for (auto [r2, c2] : ones2) {
              int key = ((n + r2 - r1) << shift) | (n + c2 - c1);

              freq[key]++;
          }
        }

        if (freq.empty()) {
          return 0;
        }

        return std::ranges::max(freq | std::views::values);
    }
};