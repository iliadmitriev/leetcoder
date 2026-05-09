
class Solution {
public:
  double mincostToHireWorkers(vector<int> &quality, vector<int> &wage, int k) {
    int n = wage.size();

    vector<pair<double, int>> rates; // cost per unit of quality, quality
    rates.reserve(n);

    for (int i = 0; i < n; ++i) {
      rates.push_back({(double)wage[i] / quality[i], quality[i]});
    }

    sort(rates.begin(), rates.end());

    double initQuality = 0.0, initRate = rates[k - 1].first;
    for (int i = 0; i < k; ++i) {
      initQuality += rates[i].second;
    }

    double minCost = initQuality * initRate;
    priority_queue<int, vector<int>, less<>> hq;

    double curQuality = 0.0;
    for (int i = 0; i < n; ++i) {
      if (hq.size() < k) {
        hq.push(rates[i].second);
        curQuality += rates[i].second;
      } else {
        curQuality += rates[i].second - hq.top();
        hq.pop();
        hq.push(rates[i].second);

        minCost = min(minCost, curQuality * rates[i].first);
      }
    }

    return minCost;
  }
};