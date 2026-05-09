class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        if (source == target) {
            return 0;
        }

        unordered_map<int, vector<int>> gr;
        int bus = 0;

        for (const auto& route : routes) {
            for (int stop: route) {
                gr[stop].push_back(bus);
            }
            bus++;
        }

        // preliminary ending: check if target or source is not on the routes
        if (gr.find(source) == gr.end() || gr.find(target) == gr.end()) {
            return -1;
        }

        queue<pair<int,int>> q;
        q.push({source, 0});
        vector<int> vis_buses(routes.size(), false);
        unordered_set<int> vis_stops;

        while (!q.empty()) {
            auto [stop, dist] = q.front(); q.pop();

            if (stop == target) {
                return dist;
            }

            for (const auto& bus: gr[stop]) {
                if (vis_buses[bus]) {
                    continue;
                }
                vis_buses[bus] = true;

                for (const auto& next_stop: routes[bus]) {
                    if (vis_stops.find(next_stop) != vis_stops.end()) {
                        continue;
                    }
                    vis_stops.insert(next_stop);

                    q.push({next_stop, dist + 1});
                }
            }
        }

        return -1;
    }
};