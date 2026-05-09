class Solution {
public:
    
    Solution() {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);
    }

    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        vector<int> x(points.size(), 0);
        for (int i = 0; i < points.size(); i++) {
            x[i] = points[i][0];
        }
        std::sort(x.begin(), x.end());

        int delta = x[1] - x[0];
        for (int i = 2; i < x.size(); i++) {
            delta = max(delta, x[i] - x[i - 1]);
        }
        return delta;
    }
};