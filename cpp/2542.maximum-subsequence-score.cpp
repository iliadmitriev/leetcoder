class Solution {
public:
    long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
        // optimization
        if (k == nums1.size()) {
            return std::accumulate(nums1.begin(), nums1.end(), (long long)0) * *std::min_element(nums2.begin(), nums2.end());
        }

        vector<pair<int, int>> data; data.reserve(nums1.size());
        for (int i = 0; i < nums1.size(); i++) {
            data.push_back(make_pair(nums2[i], nums1[i]));
        }
        std::sort(data.begin(), data.end(), [](const auto& p1, const auto& p2) -> bool {
            return p1.second > p2.second;
        });

        priority_queue<pair<int, int>, vector<pair<int, int> >, greater<> > hq(data.begin(), data.begin() + k);
        long long curSum = std::accumulate(data.begin(), data.begin() + k, (long long)0, [](long long a, const auto& p) -> long long {
            return a + p.second;
        });

        long long res = curSum * hq.top().first;

        for (int i = k; i < data.size(); i++) {
            curSum -= hq.top().second; hq.pop();
            curSum += data[i].second; hq.push(data[i]);

            res = max(res, curSum * hq.top().first);
        }

        return res;
    }
};