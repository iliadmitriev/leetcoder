#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

using std::string;
using std::unordered_map;
using std::vector;

class Solution {
public:
  int countMatches(vector<vector<string>> &items, string ruleKey,
                   string ruleValue) {
    unordered_map<string, int> types = {{"type", 0}, {"color", 1}, {"name", 2}};
    int type = types[ruleKey];
    int count = 0;

    return std::count_if(
        items.begin(), items.end(),
        [&type, &ruleValue](auto &item) { return item[type] == ruleValue; });
  }
};