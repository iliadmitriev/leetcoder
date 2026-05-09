class Solution {
public:
    int minimumTime(int n, vector<vector<int>>& relations, vector<int>& time) {
        // collect inorder vector
        // and covert graph to adjacency list
        vector<int> inorder(n, 0);
        unordered_map<int, vector<int> > graph;

        for (const auto& rel : relations) {
            inorder[rel[1] - 1]++;
            graph[rel[0] - 1].push_back(rel[1] - 1);
        }
        // start bfs from vertices with inorder == 0
        queue<int> que;
        // end times of all vertices
        vector<int> endtime(n, 0);
        for (int i = 0; i < n; i++) {
            if (inorder[i] == 0) {
                que.push(i);
                endtime[i] = time[i];
            }
        }
        int out = 0; // result - last
        while (!que.empty()) {
            auto node = que.front(); que.pop();
            out = max(out, endtime[node]);

            for (int child : graph[node]) {
                inorder[child]--;
                if (inorder[child] == 0) {
                    que.push(child);
                }
                endtime[child] = max(endtime[child], endtime[node] + time[child]);
            }
        }
        return out;
    }
};