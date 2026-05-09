struct FoodInfo {

    string name;
    string cuisine;
    int rating;

    FoodInfo() = default;
    FoodInfo(string _name, string _cuisine, int _rating): name{_name}, cuisine{_cuisine}, rating{_rating}  {}

    bool operator<(const FoodInfo& other) const {
        if (rating == other.rating) {
            return name < other.name;
        }
        return rating > other.rating;
    }

};


class FoodRatings {
private:
    unordered_map<string, FoodInfo> _foods;
    unordered_map<string, set<FoodInfo>> _cuisines;

public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        for (int i = 0; i < foods.size(); i++) {
            _foods[foods[i]] = FoodInfo(foods[i], cuisines[i], ratings[i]);
            _cuisines[cuisines[i]].insert(FoodInfo(foods[i], cuisines[i], ratings[i]));
        }
    }
    
    void changeRating(string food, int newRating) {
        auto& toUpdate = _foods[food];

        _cuisines[toUpdate.cuisine].erase(toUpdate);
        toUpdate.rating = newRating;
        _cuisines[toUpdate.cuisine].insert(toUpdate);
    }
    
    string highestRated(string cuisine) {
        return _cuisines[cuisine].begin()->name;
    }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */