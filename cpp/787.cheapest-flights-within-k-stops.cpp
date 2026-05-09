class Solution {
private:
    typedef tuple<int, int, int> Node;

public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        map<int, vector<pair<int, int>>> conn;
        for (const auto& flight : flights) {
            conn[flight[0]].push_back({flight[1], flight[2]});
        }

        priority_queue<Node, vector<Node>, greater<Node>> hq;
        hq.push({0, src, k + 1});
        vector<int> vis(n, 0);

        while (!hq.empty()) {
            auto [total, node, stops] = hq.top(); hq.pop();

            if (stops < vis[node]) {
                continue;
            }

            vis[node] = stops;

            if (node == dst) {
                return total;
            }

            for (auto [child, price] : conn[node]) {
                hq.push({total + price, child, stops - 1});
            }

        }

        return -1;
    }
};