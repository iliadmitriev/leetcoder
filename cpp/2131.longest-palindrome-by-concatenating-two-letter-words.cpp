#include <string>
#include <utility>
#include <vector>

using std::vector, std::string;

class Solution {
private:
  int getKey(const string &word) {
    return (word[0] - 'a') * 26 + (word[1] - 'a');
  }

  int getKey(const char c1, const char c2) {
    return (c1 - 'a') * 26 + c2 - 'a';
  }

  std::pair<char, char> getChar(const int key) {
    return std::make_pair(key / 26 + 'a', key % 26 + 'a');
  }

public:
  int longestPalindrome(vector<string> &words) {
    int total = 0, center = 0;
    vector<int> cache(getKey('z', 'z') + 1);

    for (const string &word : words) {
      cache[getKey(word)]++;
    }

    for (int key = 0; key < cache.size(); key++) {
      const auto [c1, c2] = getChar(key);
      const int count = cache[key];

      if (c1 == c2) {
        total += count / 2 * 4;
        if (count % 2) {
          center = 1;
        }
      } else {
        total += std::min(count, cache[getKey(c2, c1)]) * 2;
      }
    }

    return total + 2 * center;
  }
};