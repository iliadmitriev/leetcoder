class Solution {
private:
    typedef std::array<int, 2> State; // node, mask
    typedef std::array<int, 3> Data; // node, mask, distance
    typedef std::queue<Data> Queue; // Queue([node, mask, distance])
    
    // state hashing function
    struct StateHash {
        size_t operator() (const State& key) const {
            return (key[0] << 16) | key[1] ;
        }
    };

    typedef std::unordered_set<State, StateHash> Cache; // Cache([node, mask])


public:
    // Idea:

    //     BFS simultaneosly from all the nodes,
    //     marking all visited nodes.
    //     BFS garantees than first finished node is the minimal path.

    // Algorithm:

    //     1. add all nodes with their mask to queue as start nodes with 0 distance
    //         (mask with only one bit set)
    //     2. queue:
    //         2.1. get current node, it's mask and distance from queue
    //         2.2. if mask is all set to 1's then all nodes visited,
    //             so return distance
    //         2.3. iterate all neighbour nodes from current node
    //             2.3.1. check if node is not visited with current mask
    //             2.3.2. add node to visited, and add to queue with it's new mask, and new distance + 1

    // Complexity:

    //     For every starting node (n) there is 2^n combination (2 because visited or not):
    
    //     Time: O(n * 2^n)
    //     Space: O(n * 2^n)
    int shortestPathLength(vector<vector<int>>& graph) {
        int n = graph.size();

        int finish = (1 << n) - 1; // finish mask

        Queue queue; // BFS queue
        Cache cache; // visited nodes cache
        // for all nodes
        for (int i = 0; i < n; i++) {
            cache.insert({ i, (1 << i) }); // node, node mask
            queue.push({ i, (1 << i), 0 }); // node, node mask, distance = 0
        }

        while (!queue.empty()) {
            const auto [node, mask, dist] =  queue.front(); queue.pop();

            if (mask == finish) {
                return dist;
            }
            // for all adjacent nodes for current node
            for (const auto adj : graph[node]) {
                int new_mask = mask | (1 << adj);

                // if it's cached continue
                if (cache.find({ adj, new_mask }) != cache.end()) {
                    continue;
                }

                cache.insert({ adj, new_mask });
                queue.push({ adj, new_mask, dist + 1 });

            }

        }

        return std::numeric_limits<int>::max();
    }
};