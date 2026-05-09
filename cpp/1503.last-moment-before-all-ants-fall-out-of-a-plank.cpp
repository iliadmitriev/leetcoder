class Solution {
public:
    int getLastMoment(int n, vector<int>& left, vector<int>& right) {
        int max_left = 0; int min_right = n;

        for (int l: left) {
            if (l > max_left) {
                max_left = l;
            }
        }

        for (int r: right) {
            if (r < min_right) {
                min_right = r;
            }
        }

        return max(
            n - min_right,
            max_left
        );
    }
};