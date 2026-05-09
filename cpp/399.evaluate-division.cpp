typedef unordered_map<string, vector<pair<string, double>>> Graph;

class Solution {
private:
    double bfs(const string& start, const string& end, Graph& graph) {
        queue<pair<string, double>> que;
        unordered_set<string> vis;
        
        if (graph.find(start) != graph.end() && graph.find(end) != graph.end()) {
            que.push(make_pair(start, 1.0));
            vis.insert(start);
        }

        while (!que.empty()) {
            const auto [node, value] = que.front(); que.pop();

            if (node == end) {
                return value;
            }

            for (const auto [child, mul] : graph[node]) {
                if (vis.find(child) == vis.end()) {
                    que.push(make_pair(child, mul * value));
                    vis.insert(child);
                }
            }
        }

        return -1.0;
    }

public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        Graph graph;
        for (int i = 0; i < equations.size(); i++) {
            graph[equations[i][0]].push_back(make_pair(equations[i][1], values[i]));
            graph[equations[i][1]].push_back(make_pair(equations[i][0], 1 / values[i]));
        }
        // result vector with default -1.0
        vector<double> res(queries.size(), -1.0);
        for (int i = 0; i < queries.size(); i++) {
            res[i] = bfs(queries[i][0], queries[i][1], graph);
        }
        return res;
    }
};