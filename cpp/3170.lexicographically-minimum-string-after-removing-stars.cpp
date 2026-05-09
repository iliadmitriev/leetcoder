#include <queue>
#include <string>
#include <vector>

using std::string, std::priority_queue, std::vector;

class Solution {
public:
  string clearStars(string s) {
    // priority queue of char idx a = 0, .. z = 25
    priority_queue<int, vector<int>, std::greater<>> q;
    // indices of each char
    // map char -> vector of indices
    vector<vector<int>> indices(26);
    const int n = s.size();

    for (int i = 0; i < n; i++) {
      if (s[i] == '*') {
        int idx = indices[q.top()].back();
        indices[q.top()].pop_back();
        s[idx] = '*';
        if (indices[q.top()].size() == 0) {
          q.pop();
        }
        continue;
      }

      if (indices[s[i] - 'a'].size() == 0) {
        q.push(s[i] - 'a');
      }
      indices[s[i] - 'a'].push_back(i);
    }

    string res;
    for (int i = 0; i < n; i++) {
      if (s[i] != '*') {
        res += s[i];
      }
    }
    return res;
  }
};