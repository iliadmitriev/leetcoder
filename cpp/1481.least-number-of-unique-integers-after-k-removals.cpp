class Solution {
public:
    int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
        map<int, int> ch;

        for (auto num: arr) {
            ch[num]++;
        }

        priority_queue<int, vector<int>, std::greater<int>> hq;
        
        for (auto [_, v]: ch) {
            hq.push(v);
        }

        int res = hq.size();

        while (k > 0 && !hq.empty() && hq.top() <= k) {
            k -= hq.top(); hq.pop();
            res--;
        }

        return res;
    }
};