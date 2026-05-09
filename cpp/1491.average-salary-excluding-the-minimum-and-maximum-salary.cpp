class Solution {
public:
    double average(vector<int>& salary) {
        int minVal = std::numeric_limits<int>::max();
        int maxVal = 0;
        int count = -2;
        double sum = 0.0;

        for (auto sal : salary) {
            sum += sal;
            count++;
            minVal = min(minVal, sal);
            maxVal = max(maxVal, sal);
        }
        
        return (sum - minVal - maxVal) / count;
    }
};