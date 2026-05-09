class Solution {
  // rotate clockwise
  private void rot90(int[][] mat) {
    int n = mat.length; // only height, and no width (matrix should be square)

    int tmp;

    for (int i = 0; i < n / 2 + n % 2; i++) {
      for (int j = 0; j < n / 2; j++) {
        tmp = mat[i][j]; // save top left corner
        mat[i][j] = mat[n - 1 - j][i]; // move from bottom left to top left
        mat[n - 1 - j][i] = mat[n - 1 - i][n - 1 - j]; // move from bottom right to botom left
        mat[n - 1 - i][n - 1 - j] = mat[j][n - 1 - i]; // move from top right to bottom left
        mat[j][n - 1 - i] = tmp; // put saved value to top right
      }
    }

  }

  private boolean equals(int[][] mat, int[][] target) {
    int m = mat.length;
    int n = mat[0].length;

    if (m != target.length) {
      return false;
    }

    if (n != target[0].length) {
      return false;
    }

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (mat[i][j] != target[i][j]) {
          return false;
        }
      }
    }

    return true;
  }

  public boolean findRotation(int[][] mat, int[][] target) {
    if (equals(mat, target)) {
      return true;
    }

    for (int k = 0; k < 3; k++) {
      rot90(mat);

      if (equals(mat, target)) {
        return true;
      }
    }

    return false;
  }
}