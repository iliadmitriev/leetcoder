class Solution {
private:
    void dfs(int start, unordered_set<int>& vis, unordered_map<int, vector<int>>& adj, std::function<void(int)> fn) {
        stack<int> st;
        st.push(start);

        while (!st.empty()) {
            auto node = st.top(); st.pop();
            fn(node);
            for (auto child : adj[node]) {
                if (vis.find(child) != vis.end()) {
                    continue;
                }
                vis.insert(child);
                st.push(child);
            }
        }
    }

public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        // build adjacency lists
        unordered_map<int, vector<int>> adj;
        for (const auto& edge : adjacentPairs) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        // get random edge
        auto start1 = adjacentPairs[0][0];
        auto start2 = adjacentPairs[0][1];

        unordered_set<int> vis; vis.insert(start1); vis.insert(start2);
        deque<int> res;
        // start dfs from start1 collecting result to front
        dfs(start1, vis, adj, [&](int node) -> void {
            res.push_front(node);
        });
        // start dfs from start2 collecting result to back
        dfs(start2, vis, adj, [&](int node) -> void {
            res.push_back(node);
        });

        return {res.begin(), res.end()};
    }
};