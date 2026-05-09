class SmallestInfiniteSet {
private:
    int counter;
    priority_queue<int, vector<int>, greater<int>> hq;
    unordered_set<int> cache;

public:
    SmallestInfiniteSet(): counter(0), hq{}, cache{} {

    }
    
    int popSmallest() {
        if (!hq.empty()) {
            int smallest = hq.top(); hq.pop();
            cache.erase(smallest);
            return smallest;
        }

        return ++counter;
    }
    
    void addBack(int num) {
        if (num <= counter && cache.find(num) == cache.end()) {
            hq.push(num);
            cache.insert(num);
        }
    }
};

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet* obj = new SmallestInfiniteSet();
 * int param_1 = obj->popSmallest();
 * obj->addBack(num);
 */