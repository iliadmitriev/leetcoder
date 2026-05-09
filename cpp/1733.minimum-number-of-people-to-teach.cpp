#include <algorithm>
#include <bitset>
#include <vector>

using std::vector, std::bitset;

class Solution {
public:
  int minimumTeachings(int n, vector<vector<int>> &languages,
                       vector<vector<int>> &friendships) {
    typedef bitset<501> bs;
    const int m = languages.size(); // number of users
    vector<bs> users(m);            // users languages
    vector<int> common(n + 1,
                       0); // number of disconnected users with common language
    vector<bool> disconnected(m, false); // users with no common language
    int total = 0;                       // number of disconnected users

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < languages[i].size(); j++) {
        users[i][languages[i][j]] = true;
      }
    }

    for (auto &friendship : friendships) {
      int a = friendship[0] - 1, b = friendship[1] - 1;

      // if users have common language then skip
      if ((users[a] & users[b]).any()) {
        continue;
      }

      disconnected[a] = true;
      disconnected[b] = true;
    }

    for (int i = 0; i < m; i++) {
      // skip disconnected users
      if (!disconnected[i]) {
        continue;
      }

      total++;

      for (int j = 0; j < languages[i].size(); j++) {
        common[languages[i][j]]++;
      }
    }

    return total - *std::max_element(common.begin(), common.end());
  }
};