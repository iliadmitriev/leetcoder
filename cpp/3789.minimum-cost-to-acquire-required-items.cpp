class Solution {
public:
    long long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        long long total = 0LL;
        
        if (cost1 + cost2 <= costBoth) {
            total += 1LL * cost1 * need1 + 1LL * cost2 * need2;
        } else {
            int needBoth = std::min(need1, need2);
            total += 1LL * costBoth * needBoth;
            
            need1 -= needBoth;
            need2 -= needBoth;
            
            total += 1LL * need1 * std::min(cost1, costBoth);
            total += 1LL * need2 * std::min(cost2, costBoth);
        }
        
        return total;
    }
};