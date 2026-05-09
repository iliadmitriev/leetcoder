class RecentCounter {
private:
    queue<int> _q;

public:
    RecentCounter(): _q() {
        
    }
    
    int ping(int t) {
        _q.push(t);

        while (!_q.empty() && _q.front() < t - 3000) {
            _q.pop();
        }

        return _q.size();
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */