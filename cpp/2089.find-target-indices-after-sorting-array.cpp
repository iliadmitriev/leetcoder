#include <vector>
using std::vector;

class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        int count = 0, less = 0;
        for (int num : nums) {
            if (num == target) {
                count++;
            } else if (num < target) {
                less++;
            }
        }
        
        vector<int> res;
        for (int i = 0; i < count; i++) {
            res.push_back(i + less);
        }
        
        return res;
    }
};