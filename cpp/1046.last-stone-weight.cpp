class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int, vector<int>, less<>> pq(stones.begin(), stones.end());

        while (!pq.empty()) {
            auto st1 = pq.top(); pq.pop();

            if (pq.empty()) {
                return st1;
            }

            auto st2 = pq.top(); pq.pop();
            
            // if stones one grater than other 
            // put their difference back to queue
            // otherwise do nothing
            if (st1 > st2) {
                pq.push(st1 - st2);
            }
        }
        // return 0 at the end
        // all the stones vanished
        return 0;
    }
};