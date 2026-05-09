class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {

        int n = nums.size();
        deque<int> queue;
        vector<int> result(n - k + 1);

        for (int i = 0; i < n; i++) {
            // while current num is greater than rightmost element of queue
            while ( !queue.empty() && nums[queue.back()] < nums[i] ) {
                queue.pop_back(); // pop rightmost element
            }
            // push current element to monotonic queue
            queue.push_back(i);
            
            int idx = i + 1 - k;
            // skip iteration of we didn't reached the window size
            if (idx < 0)
                continue;

            // put max num (leftmost) to result
            result[idx] = nums[queue.front()];

            // drop index if current index is from the front of the queue
            if (queue.front() == idx)
                queue.pop_front();
        }
        
        return result;
    }
};