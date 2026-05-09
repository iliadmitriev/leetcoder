class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {

        int m = matrix.size(); int n = matrix[0].size(); 
        
        vector<vector<int>> prefix(m + 1, vector<int>(n + 1));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                prefix[i][j] = matrix[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1];
            }
        }

        int count = 0;
        unordered_map<int, int> cache;

        for (int r1 = 1; r1 <= m; r1++) {
            for (int r2 = r1; r2 <= m; r2++) {
                
                // refs to leetcode 560
                // https://leetcode.com/problems/subarray-sum-equals-k/description/
                cache.clear();
                cache[0] = 1;

                for (int c = 1; c <= n; c++) {
                    int total = prefix[r2][c] - prefix[r1 - 1][c];
                    count += cache[total - target];
                    cache[total]++;
                }

            }
        }

        return count;
    }
};