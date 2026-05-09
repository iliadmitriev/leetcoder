class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        // adjacency list
        unordered_map<string, vector<string>> adj;
        for (auto& ticket : tickets) {
            adj[ticket[0]].push_back(ticket[1]);
        }
        for (auto& [key, val] : adj) {
            sort(val.begin(), val.end(), greater<>());
        }

        vector<string> res;
        stack<string> st({"JFK"});

        while (!st.empty()) {
            auto des = st.top();
            if (adj[des].size()) {
                st.push(adj[des].back());
                adj[des].pop_back();
            } else {
                res.push_back(des);
                st.pop();
            }
        } 

        reverse(res.begin(), res.end());
        return res;
    }
};