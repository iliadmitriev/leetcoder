#include <vector>

using std::vector;

class Solution {
private:
public:
  int numTeams(vector<int> &rating) {
    int res = 0;

    for (int mid = 1; mid < rating.size() - 1; mid++) {
      int leftSmaller = 0, rightGreater = 0;
      for (int i = 0; i < mid; i++) {
        if (rating[i] < rating[mid])
          leftSmaller++;
      }
      for (int i = mid + 1; i < rating.size(); i++) {
        if (rating[i] > rating[mid])
          rightGreater++;
      }
      res += leftSmaller * rightGreater;

      int leftGreater = mid - leftSmaller,
          rightSmaller = rating.size() - 1 - mid - rightGreater;

      res += leftGreater * rightSmaller;
    }

    return res;
  }
};