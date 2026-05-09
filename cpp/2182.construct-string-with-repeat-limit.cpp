#include <sstream>
#include <string>
#include <utility>
#include <vector>

using std::vector, std::pair, std::string, std::stringstream;

class Solution {
public:
  string repeatLimitedString(string s, int repeatLimit) {
    vector<int> freq(26, 0);
    for (char ch : s) {
      freq[ch - 'a']++;
    }

    vector<pair<char, int>> letters;
    for (char ch = 'a'; ch <= 'z'; ch++) {
      if (freq[ch - 'a'] > 0) {
        letters.push_back({ch, freq[ch - 'a']});
      }
    }

    stringstream res;

    while (letters.size()) {
      auto [ch, count] = letters.back();
      letters.pop_back();

      if (count > repeatLimit) {
        res << string(repeatLimit, ch);
        count -= repeatLimit;

        if (letters.empty()) {
          break;
        }

        auto [nextCh, nextCount] = letters.back();
        letters.pop_back();

        res << nextCh;
        nextCount--;

        if (nextCount > 0) {
          letters.push_back({nextCh, nextCount});
        }
        letters.push_back({ch, count});
      } else {
        res << string(count, ch);
      }
    }

    return res.str();
  }
};