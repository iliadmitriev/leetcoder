#include <string>
#include <vector>
#include <bit>
#include <format>

using std::vector, std::string;

class Solution {
public:
    vector<string> readBinaryWatch(int turnedOn) {
      vector<string> res;
      
      for (uint h = 0; h < 12; h++) {
        for (uint m = 0; m < 60; m++) {
          if (std::popcount(h) + std::popcount(m) == turnedOn) {
            res.push_back(std::format("{}:{:02d}", h, m));
          }
        }
      }

      return res;
    }
};