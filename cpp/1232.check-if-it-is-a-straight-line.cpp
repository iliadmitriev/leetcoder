class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int x1 = coordinates[0][0]; int y1 = coordinates[0][1];
        int x2 = coordinates[1][0]; int y2 = coordinates[1][1];
        int x, y;

        for (int i = 2; i < coordinates.size(); i++) {
            x = coordinates[i][0]; y = coordinates[i][1];
            // (y2 - y1) / (y - y2) == (x2 - x1) / (x - x2)
            if ((y2 - y1) * (x - x2) != (x2 - x1) * (y - y2)) {
                return false;
            }
        }
        return true;
    }
};