class Solution {
public:
  vector<string> findRelativeRanks(vector<int> &score) {
    int n = score.size();
    vector<string> res(n, "");
    vector<int> places(n);
    iota(places.begin(), places.end(), 0);
    sort(places.begin(), places.end(),
         [&score](int a, int b) -> bool { return score[a] > score[b]; });

    for (int i = 0; i < n; i++) {
      res[places[i]] = to_string(i + 1);
    }

    map<int, string> ranks = {
        {0, "Gold Medal"}, {1, "Silver Medal"}, {2, "Bronze Medal"}};

    for (int i = 0; i < min(3, n); i++) {
      res[places[i]] = ranks[i];
    }

    return res;
  }
};