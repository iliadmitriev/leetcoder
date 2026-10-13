class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        const int n = nums.size();
        const int h = n / 2;

        vector<long long> sq;
        sq.reserve(n);

        std::ranges::transform(nums, std::back_inserter(sq),
                               [](int x) { return x * x; });

        auto nth = sq.begin() + h;
        std::nth_element(sq.begin(), nth, sq.end());

        long long left_sum = std::accumulate(sq.begin(), nth, 0L);
        long long right_sum = std::accumulate(nth, sq.end(), 0L);

        return right_sum - left_sum;
    }
};