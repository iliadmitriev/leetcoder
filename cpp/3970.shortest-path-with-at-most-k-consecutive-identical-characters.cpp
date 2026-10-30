#include <limits>
#include <queue>
#include <string>
#include <vector>

using std::vector, std::string, std::pair;

class Solution {
public:
    int shortestPath(int n, vector<vector<int>>& edges, string labels, int k) {
        const int INF = std::numeric_limits<int>::max();

        vector<vector<pair<int, int>>> g(
            n); // reorganize graph: g[from] = (to, weight)
        for (const auto& e : edges) {
            g[e[0]].push_back({e[1], e[2]});
        }

        // heap queue of {{path weight, node}, current repeating characters
        // streak}
        priority_queue<pair<pair<int, int>, int>,
                       vector<pair<pair<int, int>, int>>, std::greater<>>
            pq;
        // start at weight = 0, node = 0, repeating character = 1
        pq.push({{0, 0}, 1});

        // path[cur][streak] = distance from node = 0 to current node with the
        // streak
        vector<vector<int>> path(n, vector<int>(k + 1, INF));
        path[0][1] = 0; // start for 0th node

        while (pq.size()) {
            auto [inner_pair, streak] = pq.top();
            auto [dist, node] = inner_pair;
            pq.pop();

            if (dist > path[node][streak]) {
                continue;
            }

            if (node == n - 1) {
                return dist;
            }

            for (auto [nnode, weight] : g[node]) {
                int nstreak = streak + 1;
                if (labels[node] != labels[nnode]) {
                    nstreak = 1;
                }

                if (nstreak > k) {
                    continue;
                }

                int ndist = dist + weight;
                if (ndist >= path[nnode][nstreak]) {
                    continue;
                }

                path[nnode][nstreak] = ndist;
                pq.push({{ndist, nnode}, nstreak});
            }
        }

        return -1;
    }
};