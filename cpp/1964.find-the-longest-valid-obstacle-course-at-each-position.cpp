class Solution {
private:
    template<typename T>
    int binSearchRight(const vector<T>& arr, T target) {
        int lo = 0,
            hi = arr.size();

        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (target >= arr[mid]) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
public:
    vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles) {
        int n = obstacles.size();
        vector<int> dp;
        dp.reserve(n + 1);
        vector<int> res(n, 0);

        for (int i = 0; i < n; i++) {
            if (dp.empty() || dp.back() <= obstacles[i]) {
                dp.push_back(obstacles[i]);
                res[i] = dp.size();
            } else {
                int j = binSearchRight(dp, obstacles[i]);
                dp[j] = obstacles[i];
                res[i] = j + 1;
            }
        }
        return res;
    }
};