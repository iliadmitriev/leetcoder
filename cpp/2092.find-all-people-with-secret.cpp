class Solution {
private:
    void dfs(int start, const map<int, vector<int>>& adj, set<int>& vis, set<int>& res) {
        if (vis.find(start) != vis.end()) {
            return;
        }

        vis.insert(start);
        res.insert(start);

        for (auto child : adj.at(start)) {
            dfs(child, adj, vis, res);
        }
    }

public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        set<int> secrets({0, firstPerson});

        map<int, map<int, vector<int>>> timeMap;
        for (const auto& meeting : meetings) {
            timeMap[meeting[2]][meeting[0]].push_back(meeting[1]);
            timeMap[meeting[2]][meeting[1]].push_back(meeting[0]);
        }

        vector<int> timeList;
        timeList.reserve(timeMap.size());
        for (const auto& [k, _] : timeMap) {
            timeList.push_back(k);
        }
        std::sort(timeList.begin(), timeList.end());

        for (auto time : timeList) {
            set<int> visited;

            for (const auto& [src, _] : timeMap[time]) {
                if (secrets.find(src) != secrets.end()) {
                    dfs(src, timeMap[time], visited, secrets);
                }
            }
        }

        vector<int> res;
        res.assign(secrets.begin(), secrets.end());
        return res;
    }
};