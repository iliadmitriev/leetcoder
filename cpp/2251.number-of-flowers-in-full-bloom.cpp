class Solution {
public:
    vector<int> fullBloomFlowers(vector<vector<int>>& flowers, vector<int>& people) {
        vector<int> start(flowers.size());
        std::transform(flowers.begin(), flowers.end(), start.begin(), [](const auto& it) -> int { return it[0]; });
        vector<int> end(flowers.size());
        std::transform(flowers.begin(), flowers.end(), end.begin(), [](const auto& it) -> int { return it[1]; });
        std::priority_queue<int, vector<int>, std::greater<int> > startQueue(start.begin(), start.end());
        std::priority_queue<int, vector<int>, std::greater<int> > endQueue(end.begin(), end.end());

        vector<pair<int, int>> sortedPeople(people.size());
        for (int i = 0; i < people.size(); i++) {
            sortedPeople[i] = make_pair(people[i], i);
        }
        std::sort(sortedPeople.begin(), sortedPeople.end());

        vector<int> res(people.size());
        int count = 0;
        for (const auto& [p, i] : sortedPeople) {
            while (!startQueue.empty() && startQueue.top() <= p) {
                count++;
                startQueue.pop();
            }

            while (!endQueue.empty() && endQueue.top() < p) {
                count--;
                endQueue.pop();
            }
            res[i] = count;
        }
        return res;
    }
};