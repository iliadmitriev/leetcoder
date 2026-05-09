class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_map<string, bool> inorder;

        for (const auto& path : paths) {
            inorder[path[0]] = true;
        }

        for (const auto& path : paths) {
            if (!inorder[path[1]]) {
                return path[1];
            }
        }

        return "";
    }
};