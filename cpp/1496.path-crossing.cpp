class Solution {
public:
    bool isPathCrossing(string path) {
        set<pair<int, int>> cache;
        pair<int, int> cur = {0, 0};
        cache.insert(cur);

        for (auto dir: path) {
            switch (dir) {
                case 'N': cur.second++; break;
                case 'S': cur.second--; break;
                case 'E': cur.first++; break;
                case 'W': cur.first--; break;
            }
            if (cache.find(cur) != cache.end()) {
                return true;
            }
            cache.insert(cur);
        }
        return false;
    }
};