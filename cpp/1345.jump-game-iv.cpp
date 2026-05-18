#include <queue>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minJumps(std::vector<int>& arr) {
        int n = arr.size();
        if (n <= 1)
            return 0;

        // Map each value to a list of indices where it appears
        std::unordered_map<int, std::vector<int>> adj;
        for (int i = 0; i < n; ++i) {
            adj[arr[i]].push_back(i);
        }

        std::vector<bool> seen(n, false);
        std::queue<int> q;
        q.push(0);
        seen[0] = true;
        int step = 0;

        while (!q.empty()) {
            size_t level = q.size();
            while (level--) {
                int curr = q.front();
                q.pop();

                if (curr == n - 1)
                    return step;

                // Jump to i + 1
                if (curr + 1 < n && !seen[curr + 1]) {
                    seen[curr + 1] = true;
                    q.push(curr + 1);
                }
                // Jump to i - 1
                if (curr - 1 >= 0 && !seen[curr - 1]) {
                    seen[curr - 1] = true;
                    q.push(curr - 1);
                }
                // Jump to all indices with the same value
                auto it = adj.find(arr[curr]);
                if (it != adj.end()) {
                    for (int idx : it->second) {
                        if (!seen[idx]) {
                            seen[idx] = true;
                            q.push(idx);
                        }
                    }
                    // CRITICAL OPTIMIZATION: Remove after first use.
                    // Without this, duplicate-heavy arrays degrade to O(N^2).
                    adj.erase(it);
                }
            }
            step++;
        }
        return step;
    }
};