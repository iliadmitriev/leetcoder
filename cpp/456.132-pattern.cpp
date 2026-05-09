class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int lastMin = std::numeric_limits<int>::max();
        stack<pair<int, int>> st;
        
        for (auto num : nums) {

            while (!st.empty() && st.top().first < num) {
                st.pop();
            }

            if (!st.empty() && st.top().first > num && num > st.top().second) {
                return true;
            }

            st.push(make_pair(num, lastMin));
            lastMin = min(lastMin, num);
        }
        return false;
    }
};