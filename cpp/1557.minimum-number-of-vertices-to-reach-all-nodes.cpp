class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        vector<bool> indegree(n, false);
        for (const auto& edge : edges) {
            indegree[edge[1]] = true;
        }
        vector<int> res;
        for (int i = 0; i < n; i++) {
            if (!indegree[i]) {
                res.push_back(i);
            } 
        }
        return res;
    }
};