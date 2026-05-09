class Solution {
public:
    bool validateBinaryTreeNodes(int n, vector<int>& leftChild, vector<int>& rightChild) {
        // find root vertice
        vector<int> inorder(n, 0);
        for (auto r: rightChild) {
            if (r != -1) {
                inorder[r]++;
            }
        }
        for (auto l: leftChild) {
            if (l != -1) {
                inorder[l]++;
            }
        }
        int start = -1;
        for (int i = 0; i < n; i++) {
            if (inorder[i] == 0) {
                if (start != -1) { // there is more than one root
                    return false;
                }
                start = i;
            }
        }
        // root not found
        if (start == -1) {
            return false;
        }
        // dfs from start root
        // for finding cycles and chech if all vertices connected
        vector<bool> vis(n, false);
        stack<int> st; st.push(start);
        int cnt = 0;
        while (!st.empty()) {
            auto node = st.top(); st.pop();
            cnt++;

            if (leftChild[node] != -1) {
                if (vis[leftChild[node]]) {
                    return false;
                }
                vis[leftChild[node]] = true;
                st.push(leftChild[node]);
            }

           if (rightChild[node] != -1) {
                if (vis[rightChild[node]]) {
                    return false;
                }
                vis[rightChild[node]] = true;
                st.push(rightChild[node]);
            }
        }
        return cnt == n;
    }
};