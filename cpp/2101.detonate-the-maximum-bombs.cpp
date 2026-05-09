class Solution {
private:
    // returns number of vertices in a component starting from vertice
    int bfs(int start, vector<vector<int>>& graph) {
        int n = graph.size();
        int count = 0;
        
        vector<bool> vis(n, false);
        vis[start] = true;
        
        queue<int> q;
        q.push(start);

        while (!q.empty()) {
            auto node = q.front(); q.pop();
            count++;

            for (auto child : graph[node]) {
                if (!vis[child]) {
                    vis[child] = true;
                    q.push(child);
                }
            }
        }

        return count;
    }

public:
    int maximumDetonation(vector<vector<int>>& bombs) {
        // build indegree
        // build directed graph using formula for connection x^2 + y^2 <= r^2
        // sort vertices ascending using indegree
        // iterate all the vertices starting from lower indegrees
        // bfs from vertice and count number of vertices in component (component size)
        // finc max component size and return it
        int n = bombs.size();
        vector<int> indegree(n, 0);
        vector<vector<int>> graph(n, vector<int>({}));
        // build indegree and graph
        for (int i = 0; i < n; i++) {
            auto const& b1 = bombs[i];
            for (int j = 0; j < n; j++) {
                auto const& b2 = bombs[j];
                if (i != j && pow(b1[0] - b2[0], 2) + pow(b1[1] - b2[1], 2) <= pow(b1[2], 2)) {
                    graph[i].push_back(j);
                    indegree[j]++;
                }
                if (indegree[j] == n - 1) {
                    return n;
                }
            }
        }
        // sort
        vector<int> vertices(n);
        std::iota(vertices.begin(), vertices.end(), 0);
        std::sort(vertices.begin(), vertices.end(), [&indegree](int i, int j) -> bool {
            return indegree[i] < indegree[j];
        });

        int count = 0;

        for (int ver : vertices) {
            count = max(count, bfs(ver, graph));

            if (count == n) {
                return count;
            }
        }

        return count;
    }
};