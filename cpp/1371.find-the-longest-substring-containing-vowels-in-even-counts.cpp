#include <string>
#include <unordered_map>

using std::string;
using std::unordered_map;

class Solution {
public:
  int findTheLongestSubstring(string s) {
    const unordered_map<char, int> mp = {
        {'a', 0}, {'e', 1}, {'i', 2}, {'o', 3}, {'u', 4}};

    int mask = 0;
    unordered_map<int, int> cache = {{0, -1}}; // mask -> position index
    int n = s.size();
    int maxLen = 0;

    for (int i = 0; i < n; i++) {
      if (mp.find(s[i]) != mp.end()) {
        mask ^= (1 << mp.at(s[i]));
      }

      if (cache.find(mask) != cache.end()) {
        maxLen = std::max(maxLen, i - cache[mask]);
      } else {
        cache[mask] = i;
      }
    }

    return maxLen;
  }
};