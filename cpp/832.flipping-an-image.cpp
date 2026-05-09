#include <vector>

using std::vector;

class Solution {
public:
  vector<vector<int>> flipAndInvertImage(vector<vector<int>> &image) {
    int m = image.size(), n = image[0].size();

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n / 2; j++) {
        int temp = image[i][j];
        image[i][j] = 1 - image[i][n - 1 - j];
        image[i][n - 1 - j] = 1 - temp;
      }
    }

    if (n % 2) {
      for (int i = 0; i < m; i++) {
        image[i][n / 2] = 1 - image[i][n / 2];
      }
    }

    return image;
  }
};