class Solution {
public:
  int equalSubstring(string s, string t, int maxCost) {
    int cost = 0;
    int j = 0, n = s.size();
    int maxSub = 0;

    for (int i = 0; i < n; i++) {
      cost += abs(s[i] - t[i]);

      while (cost > maxCost) {
        cost -= abs(s[j] - t[j]);
        j++;
      }

      maxSub = max(maxSub, i - j + 1);
    }

    return maxSub;
  }
};