class Solution {
public:
    bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
      auto dist = [](int ax, int ay, int bx, int by) -> int {
        int dx = ax - bx, dy = ay - by;

        return dx * dx + dy * dy;
      };

      // calculate closest rectancle point coordinates to the center
      int x = std::max(x1, std::min(x2, xCenter));
      int y = std::max(y1, std::min(y2, yCenter));

      // if this point is inside the circle
      return dist(x, y, xCenter, yCenter) <= radius * radius; 
    }
};