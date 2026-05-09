const int INIT_BUCKET = int(1e6) / 8 + 1;

class MyHashSet {
private:
    unsigned char data[INIT_BUCKET];

public:
    MyHashSet() {
        memset(data, 0, sizeof(data));
    }
    
    void add(int key) {
        int page = key / 8;
        int bit = key % 8;

        data[page] |= (1 << bit);
    }
    
    void remove(int key) {
        int page = key / 8;
        int bit = key % 8;
        data[page] &= ~(1 << bit);  
    }
    
    bool contains(int key) {
       int page = key / 8;
        int bit = key % 8;

        return (data[page] & (1 << bit)) != 0;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */