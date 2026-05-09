#include <string>
#include <unordered_map>
#include <vector>

using std::string;
using std::unordered_map;
using std::vector;

class Solution {
public:
  vector<string> findRestaurant(vector<string> &list1, vector<string> &list2) {
    unordered_map<string, int> map1;
    int m = list1.size(), n = list2.size();

    for (int i = 0; i < m; i++) {
      map1[list1[i]] = i;
    }

    int minVal = m + n;
    vector<string> res;

    for (int i = 0; i < n; i++) {
      if (map1.find(list2[i]) == map1.end()) {
        continue;
      }

      if (map1[list2[i]] + i < minVal) {
        minVal = map1[list2[i]] + i;
        res.clear();
        res.push_back(list2[i]);
      } else if (map1[list2[i]] + i == minVal) {
        res.push_back(list2[i]);
      }
    }

    return res;
  }
};