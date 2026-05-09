class Solution {
private:
    typedef pair<int, int> pi;
    
    int getZero(const vector<int>& row) {
        int lo = 0;
        int hi = row.size();

        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (row[mid] == 0) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }

        return lo;
    }

public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        priority_queue<pi, vector<pi>, greater<pi>> pq;
        int j = 0;
        for (const auto& row : mat) {
            pq.push({getZero(row), j});
            j++;
        }

        vector<int> res;

        for ( ; k > 0; k--) {
            res.push_back(pq.top().second);
            pq.pop();
        }

        return res;
    }
};