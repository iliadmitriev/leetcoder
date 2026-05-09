#include <string>
#include <unordered_set>
using std::string, std::unordered_set;

class Solution {
private:
  int backtrack(const string &s, unordered_set<string> &cache, int start) {
    if (start == s.size()) {
      return cache.size();
    }

    int count = 0;

    for (int i = start; i < s.size(); i++) {
      string key = s.substr(start, i - start + 1);
      if (cache.count(key)) {
        continue;
      }

      cache.insert(key);
      count = std::max(count, backtrack(s, cache, i + 1));
      cache.erase(key);
    }

    return count;
  }

public:
  int maxUniqueSplit(string s) {
    unordered_set<string> cache;
    return backtrack(s, cache, 0);
  }
};