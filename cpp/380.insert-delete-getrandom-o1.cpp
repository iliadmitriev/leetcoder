class RandomizedSet {
private:
    unordered_map<int, int> index;
    vector<int> data;

public:
    RandomizedSet(): index({}), data({}) {}
    
    bool insert(int val) {
        if (index.find(val) != index.end()) {
            return false;
        }

        data.push_back(val);
        index[val] = data.size() - 1;
        return true;
    }
    
    bool remove(int val) {
        if (index.find(val) == index.end()) {
            return false;
        }

        int idx = index[val];
        int last = data.back();

        index[last] = idx;
        index.erase(val);

        data[idx] = last;
        data.pop_back();

        return true;
    }
    
    int getRandom() {
        return data[rand() % data.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */