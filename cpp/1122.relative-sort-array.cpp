#include <algorithm>
#include <map>
#include <vector>

using std::map;
using std::sort;
using std::vector;

class Solution {
public:
  vector<int> relativeSortArray(vector<int> &arr1, vector<int> &arr2) {
    map<int, int> order;
    for (int i = 0; i < arr2.size(); i++) {
      order[arr2[i]] = i;
    }
    sort(arr1.begin(), arr1.end(), [&order, &arr1](int a, int b) {
      int a_pos = order.count(a) ? order[a] : arr1.size() + a;
      int b_pos = order.count(b) ? order[b] : arr1.size() + b;

      return a_pos < b_pos;
    });

    return arr1;
  }
};