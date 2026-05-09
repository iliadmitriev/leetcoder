#include <algorithm>
#include <string>
#include <unordered_set>

using std::string, std::unordered_set;

class Solution {
public:
  int numJewelsInStones(string jewels, string stones) {
    unordered_set<char> jewels_set(jewels.begin(), jewels.end());

    return std::count_if(stones.begin(), stones.end(),
                         [&jewels_set](char c) -> bool {
                           return jewels_set.find(c) != jewels_set.end();
                         });
  }
};