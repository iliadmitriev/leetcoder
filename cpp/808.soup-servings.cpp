class Solution {
private:
    std::map<int, std::map<int, double>> cache;

    int z(int a) {
        return a < 0 ? 0 : a;
    }

    // C++17 hack, function to check if map has a key
    template<class Key, class Value>
    bool contains(std::map<Key, Value>& mp, Key key) {
        if (mp.find(key) == mp.end()) return false;
        return true;
    }

    double dp(int i, int j) {

        if (contains(cache, i) && contains(cache[i], j)) {
            return cache[i][j];
        }
        
        double res;

        if (i == 0 && j == 0) res = 0.5;
        else if (i == 0) res = 1.0;
        else if (j == 0) res = 0.0;
        else 
            res = ( dp(z(i - 100), j) 
                   + dp(z(i - 75), z(j - 25))
                   + dp(z(i - 50), z(j - 50)) 
                   + dp(z(i - 25), z(j - 75))
                  ) / 4.0;

        cache[i][j] = res;
        return res;

    }

public:
    double soupServings(int n) {
        if (n >= 4500) return 1.0;

        return dp(n, n);
    }
};