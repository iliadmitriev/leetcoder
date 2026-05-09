#include <string>
#include <unordered_map>
#include <vector>

using std::string;
using std::unordered_map;
using std::vector;

class Solution {
private:
  string makeKey(string &s) {
    int v[26] = {0};
    for (char c : s) {
      v[c - 'a']++;
    }

    string key;
    for (int i = 0; i < 26; i++) {
      if (v[i] > 0) {
        key.push_back(i + 'a');
      }
    }
    return key;
  }

public:
  int similarPairs(vector<string> &words) {
    unordered_map<string, int> mp;
    for (string &w : words) {
      mp[makeKey(w)]++;
    }

    int res = 0;

    for (auto [_, v] : mp) {
      res += v * (v - 1) / 2;
    }

    return res;
  }
};