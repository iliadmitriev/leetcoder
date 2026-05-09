class Solution {
private:
    int left(const vector<int>& arr, int target) {
        int lo = 0; int hi = arr.size();
        int mid;
        while (lo < hi) {
            mid = (lo + hi) / 2;
            if (arr[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
    int right(const vector<int>& arr, int target) {
        int lo = 0; int hi = arr.size();
        int mid;
        while (lo < hi) {
            mid = (lo + hi) / 2;
            if (arr[mid] <= target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }

public:
    vector<int> platesBetweenCandles(string s, vector<vector<int>>& queries) {
        // convert string of '**|***|**|' to plates counts (2,3,2)
        // and indices of pipes (2,6,9)
        vector<int> plates;
        vector<int> indices;
        int currCount = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '*') {
                currCount++;
            } else if (s[i] == '|') {
                plates.push_back(currCount);
                indices.push_back(i);
                currCount = 0;
            }
        }
        // convert plate counts to accumulated vector
        // 1,2,3,2 -> 1,3,6,8
        vector<int> acc_plates(plates.size(), 0);
        std::partial_sum(plates.begin(), plates.end(), acc_plates.begin());
        // process queries with binary search
        // and add to result
        vector<int> res; res.reserve(queries.size());
        for (const auto& q : queries) {
            auto l = left(indices, q[0]);
            auto r = right(indices, q[1]);
            if (l < acc_plates.size() && r - 1 < acc_plates.size() && l != r) {
                res.push_back(acc_plates[r - 1] - acc_plates[l]);
            } else {
                res.push_back(0);
            }
        }
        return res;
    }
};