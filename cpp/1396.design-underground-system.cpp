class UndergroundSystem {
private:
    typedef string Key; // startStation, endStaion
    unordered_map<Key, int> count;
    unordered_map<Key, double> time;
    unordered_map<int, pair<string, int>> check;

public:
    UndergroundSystem() : count(), time(), check() {
    }
    
    void checkIn(int id, string stationName, int t) {
        check[id] = make_pair(stationName, t);
    }
    
    void checkOut(int id, string stationName, int t) {
        auto [startStation, t1] = check[id];
        // key = startStation, endStaion
        auto key = startStation + "*" + stationName;
        count[key]++;
        time[key] += t - t1;
    }
    
    double getAverageTime(string startStation, string endStation) {
        auto key = startStation + "*" + endStation;
        return time[key] / double(count.find(key) != count.end() ? count[key] : 1.0);
    }
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */