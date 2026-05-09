#include <vector>

using std::vector;

class Solution {
public:
  int countGoodRectangles(vector<vector<int>> &rectangles) {
    int maxSquare = 0, countSquares = 0;

    for (auto &rect : rectangles) {
      int square = std::min(rect[0], rect[1]);
      if (square > maxSquare) {
        maxSquare = square;
        countSquares = 1;
      } else if (square == maxSquare) {
        countSquares++;
      }
    }

    return countSquares;
  }
};