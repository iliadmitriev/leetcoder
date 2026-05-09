class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        size_t n = temperatures.size();
        vector<int> res(n, 0);
        
        stack<int> st;

        for (int j = 0; j < n; j++) {
            while (!st.empty() && temperatures[st.top()] < temperatures[j]) {
                res[st.top()] = j - st.top();
                st.pop();
            }
            st.push(j);
        }

        return res;
    }
};