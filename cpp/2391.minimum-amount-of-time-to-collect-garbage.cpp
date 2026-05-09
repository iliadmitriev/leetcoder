class Solution {
public:
    int garbageCollection(vector<string>& garbage, vector<int>& travel) {
        int total = 0;
        int f = 0, g = 0, p = 0, m = 0;

        for (int i = 0; i < garbage.size(); i++) {
            total += garbage[i].size();

            if (i > 0) {
                f += travel[i - 1];
            }

            if (garbage[i].find('M') != std::string::npos) {
                m = f;
            }
            if (garbage[i].find('P') != std::string::npos) {
                p = f;
            }
            if (garbage[i].find('G') != std::string::npos) {
                g = f;
            }
        }

        return total + m + p + g;
    }
};