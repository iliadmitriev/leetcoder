class Solution {

public:
  vector<vector<int>> spiralMatrix(int m, int n, ListNode *head) {

    auto getNext = [&head]() -> int {
      if (head) {
        int x = head->val;
        head = head->next;
        return x;
      }
      return -1;
    };

    vector<vector<int>> res(m, vector<int>(n, -1));

    int top = 0, left = 0, bottom = m - 1, right = n - 1;

    while (top < bottom && left < right) {

      for (int i = left; i < right; i++)
        res[top][i] = getNext();

      for (int i = top; i < bottom; i++)
        res[i][right] = getNext();

      for (int i = right; i > left; i--)
        res[bottom][i] = getNext();

      for (int i = bottom; i > top; i--)
        res[i][left] = getNext();

      top++, left++, bottom--, right--;
    }

    for (int i = top; i <= bottom; i++)
      for (int j = left; j <= right; j++)
        res[i][j] = getNext();

    return res;
  }
};