class Solution {
public:
    int eliminateMaximum(vector<int>& dist, vector<int>& speed) {
        int n = dist.size();
        // count number of monsters arrived at any minute
        vector<int> arrive(n);
        for (int i = 0; i < n; i++) {
            int num = ceil(double(dist[i]) / double(speed[i]));
            if (num < n) {
                arrive[num]++;
            }
        }
        
        for (int i = 1; i < n; i++) {
            // convert to accumulative 
            arrive[i] += arrive[i - 1];
            // if at any moment in time count of monsters arrived
            // more than can be killed 
            if (arrive[i] > i) {
                return i;
            }
        }
        return n;
    }
};