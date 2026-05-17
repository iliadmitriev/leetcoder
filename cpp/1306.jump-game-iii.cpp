class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        const int n = arr.size();
        vector<bool> vis(n, false);

        auto dfs = [&vis, &arr, n](auto&& self, int i) -> bool {
          
            if (arr[i] == 0) {
               return true;
            }
            
            if (vis[i]) {
                return false;
            }
            vis[i] = true;

            if (i + arr[i] < n && self(self, i + arr[i])) {
              return true;
            }
            
            return i - arr[i] >= 0 && self(self, i - arr[i]);
        };

        return dfs(dfs, start);
    }
};