#include <algorithm>
#include <map>
#include <sstream>
#include <string>

using namespace std;

class Solution {
public:
  string frequencySort(string s) {
    map<char, int> counts;
    for (char ch : s) {
      counts[ch]++;
    }

    vector<pair<char, int>> cache;
    std::copy(begin(counts), end(counts), back_inserter(cache));
    std::sort(begin(cache), end(cache), [](auto &a, auto &b) -> bool {
      return a.second == b.second ? a.first < b.first : a.second > b.second;
    });

    stringstream res;
    for (auto [ch, cnt] : cache) {
      for (int i = 0; i < cnt; i++) {
        res << ch;
      }
    }

    return res.str();
  }
};
