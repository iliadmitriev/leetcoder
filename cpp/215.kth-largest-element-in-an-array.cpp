class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        std::priority_queue<int, std::vector<int>, std::greater<int>> heap(nums.begin(), nums.begin() + k);

        for (int i = k; i < nums.size(); i++)
            if (nums[i] > heap.top()) {
                heap.pop();
                heap.push(nums[i]);
            };

        return heap.top();
    }
};