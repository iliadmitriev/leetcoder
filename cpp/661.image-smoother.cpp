class Solution {
private:
    int avg(vector<vector<int>>& arr, int y, int x, int l = 3) {
        int res = 0, cnt = 0;
        int m = arr.size(); int n = arr[0].size();
        for (int i = -(l / 2); i <= l / 2; i++) {
            for (int j = -(l / 2); j <= l / 2; j++) {
                if (0 > y + i || y + i >= m || 0 > x + j || x + j >= n) {
                    continue;
                }
                cnt++; res += arr[y + i][x + j];
            }
        }
        return res / cnt;
    }
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& img) {
        int m = img.size(); int n = img[0].size();
        vector<vector<int>> res(m, vector<int>(n, 0));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                res[i][j] = avg(img, i, j);
            }
        }
        return res;
    }
};