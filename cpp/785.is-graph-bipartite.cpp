class Solution {
private:
    bool bfs(int node, vector<int>& colors, vector<vector<int>>& graph) {
        queue<int> que;
        que.push(node);
        colors[node] = 0; // start black

        while (!que.empty()) {
            node = que.front(); que.pop();

            for (const auto& child: graph[node]) {
                if (colors[child] == -1) {
                    colors[child] = 1 - colors[node];
                    que.push(child);
                } else if (colors[child] != 1 - colors[node]) {
                    return false;
                }
            }
        }
        return true;
    }
public:
    bool isBipartite(vector<vector<int>>& graph) {
        // colors 0 - red, 1 - black -1 - not colored
        vector<int> colors(graph.size(), -1);
        
        for (int i = 0; i < graph.size(); i++) {
            if (colors[i] == -1 && !bfs(i, colors, graph)) {
                return false;
            }
        }

        return true;
    }
};