#include <unordered_map>
#include <vector>

using std::unordered_map;
using std::vector;

class Solution {
public:
  bool canFormArray(vector<int> &arr, vector<vector<int>> &pieces) {
    unordered_map<int, vector<int> *> keys;
    for (auto &piece : pieces) {
      keys[piece[0]] = &piece;
    }

    if (keys.find(arr[0]) == keys.end()) {
      return false;
    }

    vector<int> *p = keys[arr[0]];
    int i = 0, j = 0;
    while (i < arr.size()) {

      if (j == p->size()) {
        if (keys.find(arr[i]) == keys.end()) {
          return false;
        }

        p = keys[arr[i]];
        j = 0;
      }

      if (arr[i] != (*p)[j]) {
        return false;
      }

      i++;
      j++;
    }

    return true;
  }
};