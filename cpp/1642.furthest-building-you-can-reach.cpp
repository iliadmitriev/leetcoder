class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        
        int diff;
        priority_queue<int, vector<int>, less<int>> hq;

        for (int i = 0; i < heights.size() - 1; i++) {
            diff = heights[i + 1] - heights[i];
            
            if (diff <= 0) {
                continue;
            }

            bricks -= diff;
            hq.push(diff);

            if (bricks < 0) {
                if (ladders == 0) {
                    return i;
                }

                ladders -= 1;
                bricks += hq.top(); hq.pop();
            }
        }

        return heights.size() - 1;
    }
};