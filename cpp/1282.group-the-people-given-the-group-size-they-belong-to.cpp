class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        
        vector<pair<int, int>> groups;
        for (auto j = 0; j < groupSizes.size(); j++) {
            groups.push_back(make_pair(groupSizes[j], j));
        }
        sort(groups.begin(), groups.end());

        vector<vector<int>> assigned;
        vector<int> currGroup;

        for (auto& [groupSize, person] : groups) {
            currGroup.push_back(person);
            
            if (currGroup.size() == groupSize) {
                assigned.push_back(currGroup);
                currGroup.clear();
            }
        }

        return assigned;
    }
};