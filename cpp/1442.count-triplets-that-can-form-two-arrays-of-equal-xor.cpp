class Solution {
public:
  int countTriplets(vector<int> &arr) {
    int n = arr.size();
    int count = 0;
    int a;

    for (int i = 0; i < n - 1; i++) {
      a = arr[i];
      for (int j = i + 1; j < n; j++) {
        a ^= arr[j];
        if (a == 0) {
          count += j - i;
        }
      }
    }

    return count;
  }
};