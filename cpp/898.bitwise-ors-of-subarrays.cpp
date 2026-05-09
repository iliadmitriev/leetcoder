#include <unordered_set>
#include <vector>

using std::vector, std::unordered_set;

class Solution {
public:
  int subarrayBitwiseORs(vector<int> &arr) {
    unordered_set<int> s;

    for (int i = 0; i < arr.size(); i++) {
      int x = arr[i];
      s.insert(x);

      int skip = 0, take = x;

      for (int j = i - 1; j >= 0; j--) {
        skip |= arr[j];
        take = skip | x;
        if (skip == take) {
          break;
        }

        s.insert(take);
      }
    }

    return s.size();
  }
};