#include <string>
#include <unordered_map>
#include <vector>

using std::string;
using std::unordered_map;
using std::vector;

class Solution {
public:
  int maximumNumberOfStringPairs(vector<string> &words) {
    unordered_map<string, int> mp;
    int count = 0;

    for (string &word : words) {
      if (mp.count(string(word.rbegin(), word.rend()))) {
        count++;
      }
      mp[word]++;
    }

    return count;
  }
};